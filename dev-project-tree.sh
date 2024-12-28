#!/bin/bash

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

# Obtener el directorio donde está el script
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
CONFIG_FILE="$SCRIPT_DIR/exclude-patterns.json"

# Cargar patrones desde JSON
load_patterns() {
    if ! command -v jq &> /dev/null; then
        echo "Error: jq es necesario para este script"
        exit 1
    fi

    EXCLUDES=($(jq -r '.exclude[]' "$CONFIG_FILE"))
}

# Construir patrón de exclusión
build_exclude_pattern() {
    local patterns=("$@")
    local result=""
    for pattern in "${patterns[@]}"; do
        result="$result -not -path '*/$pattern/*' -not -name '$pattern'"
    done
    echo "$result"
}

# Cargar patrones
load_patterns

# Construir y ejecutar comando find
CMD="find . $(build_exclude_pattern "${EXCLUDES[@]}")"

# Ejecutar y formatear como árbol
echo -e "${GREEN}Estructura del proyecto:${NC}"
eval "$CMD" | sed -e "s/[^-][^\/]*\//  │   /g" \
                  -e "s/│   \([^│]\)/│   ├── \1/" \
                  -e "s/│   │/│   ├/" \
                  -e "s/├── │/├── /" \
                  -e "s/└── │/└── /" \
                  -e "s/  │   └/  └──/"

echo -e "\n${BLUE}Nota:${NC} Excluyendo dependencias y archivos temporales"
