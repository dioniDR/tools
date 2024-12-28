#!/usr/bin/env python3

import os
import sys
from datetime import datetime

class QuickNote:
    def __init__(self):
        self.notes = {
            "ccmd": """
=== Uso de ccmd ===
Función para ejecutar comandos y copiar su salida al portapapeles.

Ejemplo:
ccmd 'ls -la'
ccmd 'cat archivo.txt'
""",
            "bashrc": """
=== Archivo .bashrc ===
Ubicación: ~/.bashrc
Ver contenido: cat ~/.bashrc
Recargar: source ~/.bashrc
""",
            "alias": """
=== Ver alias ===
Ver todos: alias
Agregar nuevo: echo "alias nombre='comando'" >> ~/.bashrc
""",
            "terminal_collector": """
=== Uso de terminal_collector.sh ===
Recopila salidas de varios comandos.

Ejemplo con 2 comandos:
terminal_collector.sh "ccmd 'ls -la'" "pwd"
"""
        }

    def show(self, topic=None):
        if not topic:
            print("\n=== Temas disponibles ===")
            for key in self.notes.keys():
                print(f"- {key}")
            return

        if topic in self.notes:
            print(self.notes[topic])
        else:
            print(f"❌ Tema no encontrado. Temas disponibles: {', '.join(self.notes.keys())}")

def main():
    qnote = QuickNote()
    
    if len(sys.argv) > 1:
        qnote.show(sys.argv[1])
    else:
        qnote.show()

if __name__ == "__main__":
    main()
