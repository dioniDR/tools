#!/usr/bin/env python3
import os
import re
import ast
import json
import difflib
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional

class CodeInserter:
    @staticmethod
    def insert_at_line(content: str, line_number: int, new_content: str) -> str:
        lines = content.splitlines()
        lines.insert(line_number - 1, new_content)
        return '\n'.join(lines)
    
    @staticmethod
    def insert_after_pattern(content: str, pattern: str, new_content: str) -> str:
        lines = content.splitlines()
        last_match = -1
        
        # Encontrar la última coincidencia del patrón
        for i, line in enumerate(lines):
            if re.search(pattern, line):
                last_match = i
        
        if last_match != -1:
            lines.insert(last_match + 1, new_content)
            return '\n'.join(lines)
        return content

class CodeModifier:
    @staticmethod
    def modify_range(content: str, start_line: int, end_line: int, new_content: str) -> str:
        lines = content.splitlines()
        lines[start_line-1:end_line] = new_content.splitlines()
        return '\n'.join(lines)
    
    @staticmethod
    def comment_range(content: str, start_line: int, end_line: int, ext: str) -> str:
        lines = content.splitlines()
        comment_char = '#' if ext in ['.py', '.sh'] else '//'
        
        for i in range(start_line-1, end_line):
            if not lines[i].strip().startswith(comment_char):
                lines[i] = f"{comment_char} {lines[i]}"
        
        return '\n'.join(lines)

class CodeFinder:
    def __init__(self, base_dir: str):
        self.base_dir = os.path.expanduser(base_dir)
        self.inserter = CodeInserter()
        self.modifier = CodeModifier()

    def process_changes(self, changes_file: str) -> Dict[str, List[str]]:
        with open(changes_file) as f:
            changes = json.load(f)
        
        results = {'modified': [], 'errors': []}
        
        for change in changes:
            try:
                filepath = os.path.join(self.base_dir, change['file'])
                with open(filepath, 'r') as f:
                    content = f.read()
                
                new_content = content
                if 'line' in change:
                    new_content = self.inserter.insert_at_line(
                        new_content, change['line'], change['content']
                    )
                elif 'pattern' in change:
                    new_content = self.inserter.insert_after_pattern(
                        new_content, change['pattern'], change['content']
                    )
                elif 'range' in change:
                    start, end = map(int, change['range'].split('-'))
                    new_content = self.modifier.modify_range(
                        new_content, start, end, change['content']
                    )
                
                if new_content != content:
                    if change.get('preview'):
                        self._show_diff(content, new_content)
                    else:
                        with open(filepath, 'w') as f:
                            f.write(new_content)
                        results['modified'].append(filepath)
                
            except Exception as e:
                results['errors'].append(f"Error en {change.get('file')}: {str(e)}")
        
        return results

    def _show_diff(self, old_content: str, new_content: str):
        diff = difflib.unified_diff(
            old_content.splitlines(keepends=True),
            new_content.splitlines(keepends=True)
        )
        print(''.join(diff))

def main():
    parser = argparse.ArgumentParser(description='Code Finder 2.0 - Herramienta de modificación de código')
    parser.add_argument('--path', default=".", help='Directorio base')
    parser.add_argument('--changes', help='Archivo JSON con cambios múltiples')
    parser.add_argument('--line', type=int, help='Número de línea para inserción')
    parser.add_argument('--insert', help='Contenido a insertar')
    parser.add_argument('--pattern', help='Patrón para insertar después')
    parser.add_argument('--range', help='Rango de líneas (ejemplo: 10-15)')
    parser.add_argument('--replace', help='Contenido para reemplazar')
    parser.add_argument('--comment', help='Rango de líneas para comentar')
    parser.add_argument('--preview', action='store_true', help='Mostrar cambios sin aplicar')
    parser.add_argument('--file-pattern', help='Patrón de archivo')
    
    args = parser.parse_args()
    finder = CodeFinder(args.path)
    
    if args.changes:
        results = finder.process_changes(args.changes)
        if results['modified']:
            print("\nArchivos modificados:")
            for file in results['modified']:
                print(f"✓ {file}")
        if results['errors']:
            print("\nErrores encontrados:")
            for error in results['errors']:
                print(f"✗ {error}")

if __name__ == "__main__":
    main()
