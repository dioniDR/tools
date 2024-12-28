#!/usr/bin/env python3
import subprocess
import sys

def copy_to_clipboard(text):
    subprocess.run(["xclip", "-sel", "clip"], input=text.encode())

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        copy_to_clipboard(result.stdout)
        print("✓ Salida copiada al portapapeles")
    return result.stdout, result.stderr

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ccmd 'command'")
    else:
        command = " ".join(sys.argv[1:])
        run_command(command)
