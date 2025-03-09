# Terminal Fusion

Un conjunto de herramientas para desarrolladores que facilita la gestión, búsqueda y manipulación de código así como la integración con interfaces web.

## 📋 Descripción General

Terminal Fusion es una colección de scripts y utilidades diseñadas para aumentar la productividad durante el desarrollo de software. Incluye herramientas para la gestión de notas de desarrollo, manipulación de código, análisis de proyectos y la integración entre terminal y navegador web.

## 🔧 Herramientas Principales

### Manipulación de Código

- **code_finder.py**: Herramienta avanzada para buscar, insertar y modificar código en archivos de proyectos.
  ```bash
  python code_finder.py --path "/ruta/proyecto" --file-pattern "*.py" --line 10 --insert "nuevo_código"
  ```

- **fix-extension.sh**: Script para corregir problemas en la extensión de navegador de Terminal Fusion.
  ```bash
  ./fix-extension.sh
  ```

### Utilidades del Sistema

- **ccmd.py**: Ejecuta comandos y copia la salida al portapapeles automáticamente.
  ```bash
  ccmd 'ls -la'
  ```

- **clean_pycache.py**: Limpia directorios __pycache__ para liberar espacio.
  ```bash
  ./clean_pycache.py
  ```

- **terminal_collector.py**: Recopila salidas de varios comandos en un solo documento.
  ```bash
  ./terminal_collector.py "ls -la" "ps aux" "free -h"
  ```

### Visualización de Proyectos

- **dev-project-tree.sh**: Genera una representación visual de la estructura del proyecto, excluyendo archivos y directorios específicos definidos en `exclude-patterns.json`.
  ```bash
  ./dev-project-tree.sh
  ```

### Sistema de Notas

- **dev_notes.py**: Sistema completo para gestionar notas técnicas organizadas en categorías.
  ```bash
  # Agregar una nota
  ./dev_notes.py add --category debug --content "Solución al problema X" --tags "error,solución"
  
  # Buscar notas
  ./dev_notes.py search --query "error" --category debug
  
  # Listar notas
  ./dev_notes.py list --category system
  ```

- **qnote.py**: Acceso rápido a notas comunes y fragmentos útiles.
  ```bash
  ./qnote.py bashrc
  ```

### Integración con Web

- **launch-terminal-fusion.sh**: Inicia los servidores backend (FastAPI) y frontend para la interfaz web de Terminal Fusion.
  ```bash
  ./launch-terminal-fusion.sh
  ```

## 🗂️ Estructura de Archivos

```
terminal-fusion/
├── ccmd.py                      # Ejecuta comandos y copia salida
├── clean_pycache.py             # Limpia directorios __pycache__
├── code_finder.py               # Busca y modifica código
├── dev-project-tree.sh          # Muestra estructura de proyecto
├── dev_notes.py                 # Sistema de notas completo
├── exclude-patterns.json        # Patrones de exclusión para dev-project-tree
├── fix-extension.sh             # Corrige extensión web
├── launch-terminal-fusion.sh    # Inicia servidores web
├── qnote.py                     # Notas rápidas
├── terminal_collector.py        # Recolecta salidas de comandos
└── notes/                       # Directorio de notas
    ├── system/                  # Notas del sistema
    ├── debug/                   # Notas de depuración
    ├── commands/                # Notas de comandos útiles
    ├── ideas/                   # Ideas y mejoras
    ├── learn/                   # Aprendizajes
    └── todo/                    # Tareas pendientes
```

## 🚀 Instalación

1. Clone el repositorio:
   ```bash
   git clone <url-repositorio>
   ```

2. Configure los permisos de ejecución:
   ```bash
   chmod +x *.py *.sh
   ```

3. Asegúrese de que sus scripts estén en el PATH (recomendado: ~/bin)

## 📝 Requisitos

- Python 3.7+
- Node.js (para la extensión y frontend)
- Paquetes requeridos:
  - `xclip` (para ccmd.py)
  - `jq` (para dev-project-tree.sh)

## 📚 Categorías de Notas

El sistema de notas se organiza en las siguientes categorías:

- **system**: Notas relacionadas con la configuración del sistema
- **debug**: Notas sobre depuración y solución de problemas
- **commands**: Comandos útiles para referencia rápida
- **ideas**: Ideas para mejoras futuras
- **learn**: Conocimientos adquiridos durante el desarrollo
- **todo**: Tareas pendientes y seguimiento de proyectos

## 🛠️ Integración con Web

Terminal Fusion incluye una interfaz web que complementa las herramientas de línea de comandos. La integración consta de:

1. **Servidor Backend (FastAPI)**: Gestiona la comunicación entre la terminal y la interfaz web
2. **Aplicación Frontend**: Interfaz de usuario construida con tecnologías web modernas
3. **Extensión de Navegador**: Permite la integración directa con páginas web

## 📄 Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).

## 👥 Contribución

Las contribuciones son bienvenidas. Por favor, siga estos pasos:

1. Haga fork del repositorio
2. Cree una nueva rama (`git checkout -b feature/nueva-caracteristica`)
3. Confirme sus cambios (`git commit -m 'Añade nueva característica'`)
4. Envíe a la rama (`git push origin feature/nueva-caracteristica`)
5. Abra un Pull Request
