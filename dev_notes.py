#!/usr/bin/env python3

import os
import sys
from datetime import datetime
import argparse
import subprocess

class DevNotes:
    def __init__(self):
        self.notes_dir = os.path.expanduser("~/bin/tools/notes")
        self.categories = {
            "system": "Notas del sistema",
            "debug": "Debugging y solución de problemas",
            "commands": "Comandos útiles",
            "ideas": "Ideas y mejoras",
            "learn": "Aprendizajes",
            "todo": "Tareas pendientes"
        }
        self._ensure_dirs()

    def _ensure_dirs(self):
        """Crea la estructura de directorios necesaria"""
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)
            for category in self.categories:
                os.makedirs(os.path.join(self.notes_dir, category))

    def add_note(self, category: str, content: str, tags: list = None):
        """Agrega una nueva nota"""
        if category not in self.categories:
            print(f"❌ Categoría no válida. Opciones: {', '.join(self.categories)}")
            return False

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.notes_dir, category, f"note_{timestamp}.md")

        with open(filename, 'w') as f:
            f.write(f"# Nota {timestamp}\n\n")
            if tags:
                f.write(f"Tags: {', '.join(tags)}\n\n")
            f.write(content)

        print(f"✅ Nota guardada en {filename}")
        return True

    def search_notes(self, query: str, category: str = None):
        """Busca en las notas"""
        command = ["grep", "-r", "-i", query]
        
        if category:
            search_path = os.path.join(self.notes_dir, category)
        else:
            search_path = self.notes_dir

        command.append(search_path)
        
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            if result.stdout:
                print("\n=== Resultados encontrados ===")
                print(result.stdout)
            else:
                print("❌ No se encontraron resultados")
        except Exception as e:
            print(f"❌ Error en la búsqueda: {str(e)}")

    def list_notes(self, category: str = None):
        """Lista las notas existentes"""
        if category and category not in self.categories:
            print(f"❌ Categoría no válida. Opciones: {', '.join(self.categories)}")
            return

        for cat in self.categories if not category else [category]:
            cat_path = os.path.join(self.notes_dir, cat)
            if os.path.exists(cat_path):
                notes = os.listdir(cat_path)
                if notes:
                    print(f"\n=== {self.categories[cat]} ===")
                    for note in sorted(notes):
                        print(f"📝 {note}")

def main():
    parser = argparse.ArgumentParser(description='DevNotes - Sistema de notas para desarrollo')
    parser.add_argument('action', choices=['add', 'search', 'list'], help='Acción a realizar')
    parser.add_argument('--category', '-c', help='Categoría de la nota')
    parser.add_argument('--content', help='Contenido de la nota')
    parser.add_argument('--tags', help='Tags separados por comas')
    parser.add_argument('--query', '-q', help='Término de búsqueda')

    args = parser.parse_args()
    notes = DevNotes()

    if args.action == 'add':
        if not args.category or not args.content:
            print("❌ Se requiere categoría y contenido para agregar una nota")
            return
        tags = args.tags.split(',') if args.tags else None
        notes.add_note(args.category, args.content, tags)

    elif args.action == 'search':
        if not args.query:
            print("❌ Se requiere un término de búsqueda")
            return
        notes.search_notes(args.query, args.category)

    elif args.action == 'list':
        notes.list_notes(args.category)

if __name__ == "__main__":
    main()
