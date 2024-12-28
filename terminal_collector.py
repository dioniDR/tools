#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime
from ccmd import copy_to_clipboard, run_command

def collect_outputs(commands):
   """Recolecta la salida de múltiples comandos y la copia al portapapeles"""
   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   output = [f"=== Sistema Check {timestamp} ===\n"]
   
   for cmd in commands:
       output.append(f"=== {cmd} ===")
       stdout, stderr = run_command(cmd)
       output.extend([stdout or "", stderr or ""])
   
   final_output = "\n".join(output)
   copy_to_clipboard(final_output)
   return final_output

if __name__ == "__main__":
   # Si se pasan argumentos, usarlos como comandos
   # Si no, usar los comandos predeterminados
   commands = sys.argv[1:] if len(sys.argv) > 1 else [
       "ls -la ~/bin/lib/core/",
       "ls -la ~/bin/lib/commands/",
       "cat ~/bin/lib/core/__init__.py",
   ]
   print(collect_outputs(commands))
