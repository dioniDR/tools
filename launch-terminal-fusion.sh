#!/bin/bash

# Colores para los mensajes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Función para imprimir mensajes con formato
print_status() {
    echo -e "${BLUE}[Terminal Fusion]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

# Directorio base del proyecto
PROJECT_DIR="$HOME/bin/terminal-fusion"

# Verificar que estamos en el directorio correcto
if [ ! -d "$PROJECT_DIR" ]; then
    print_error "No se encontró el directorio del proyecto"
    exit 1
fi

# Función para detener servidores al salir
cleanup() {
    print_status "Deteniendo servidores..."
    kill $(jobs -p) 2>/dev/null
    exit 0
}

trap cleanup SIGINT SIGTERM

# Iniciar servidor FastAPI
print_status "Iniciando servidor FastAPI..."
cd "$PROJECT_DIR/server"
source venv/bin/activate
python -m uvicorn src.main:app --reload &
FASTAPI_PID=$!
sleep 2

if kill -0 $FASTAPI_PID 2>/dev/null; then
    print_success "Servidor FastAPI iniciado en http://localhost:8000"
else
    print_error "Error al iniciar servidor FastAPI"
    cleanup
fi

# Iniciar servidor Frontend
print_status "Iniciando servidor Frontend..."
cd "$PROJECT_DIR/web"
npm run dev &
VITE_PID=$!
sleep 2

if kill -0 $VITE_PID 2>/dev/null; then
    print_success "Servidor Frontend iniciado en http://localhost:5173"
else
    print_error "Error al iniciar servidor Frontend"
    cleanup
fi

# Abrir en el navegador predeterminado
print_status "Abriendo aplicación en el navegador..."
sleep 2
if command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:5173
elif command -v open &> /dev/null; then
    open http://localhost:5173
else
    print_error "No se pudo abrir el navegador automáticamente"
    print_status "Por favor, abre http://localhost:5173 manualmente"
fi

print_success "Terminal Fusion está ejecutándose"
print_status "Presiona Ctrl+C para detener todos los servidores"

# Mantener el script ejecutándose y mostrar logs
wait
