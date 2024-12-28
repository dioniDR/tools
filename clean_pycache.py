#!/usr/bin/env python3
# clean_pycache.py

import os
import shutil
from pathlib import Path

def clean_pycache():
   """Limpia todos los directorios __pycache__ en el proyecto P2"""
   base_dir = Path(os.path.expanduser("~/bin"))
   
   # Encontrar todos los directorios __pycache__
   pycache_dirs = []
   for root, dirs, _ in os.walk(base_dir):
       if "__pycache__" in dirs:
           pycache_dirs.append(Path(root) / "__pycache__")
   
   if not pycache_dirs:
       print("✨ No se encontraron directorios de caché")
       return
   
   # Mostrar directorios encontrados
   print("🔍 Directorios de caché encontrados:")
   for cache_dir in pycache_dirs:
       print(f"  • {cache_dir}")
   
   # Limpiar cada directorio
   print("\n🧹 Limpiando caché...")
   for cache_dir in pycache_dirs:
       try:
           if cache_dir.exists():
               size_before = sum(f.stat().st_size for f in cache_dir.glob('*'))
               shutil.rmtree(cache_dir)
               print(f"✅ Limpiado: {cache_dir} ({size_before/1024:.1f}KB liberados)")
       except Exception as e:
           print(f"❌ Error al limpiar {cache_dir}: {str(e)}")
   
   print("\n✨ Limpieza completada!")

if __name__ == "__main__":
   clean_pycache()
