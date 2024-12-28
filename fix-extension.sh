#!/bin/bash

# Colores para mensajes
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}[*] Fixing Terminal Fusion Extension...${NC}"

# Directorio base
EXT_DIR="$HOME/bin/terminal-fusion/extension"

# Crear archivo content.ts con el código de Terminal Overlay
echo -e "${GREEN}[+] Creating content.ts...${NC}"
cat > "$EXT_DIR/src/content.ts" << 'EOL'
type Position = {
  x: number;
  y: number;
};

class TerminalOverlay {
  // ... (contenido actual de manifest.json)
}
EOL

# Crear el manifest.json correcto
echo -e "${GREEN}[+] Creating manifest.json...${NC}"
cat > "$EXT_DIR/public/manifest.json" << 'EOL'
{
  "manifest_version": 3,
  "name": "Terminal Fusion",
  "version": "1.0.0",
  "description": "Terminal integration with web interface",
  "permissions": [
    "webNavigation",
    "tabs",
    "storage",
    "activeTab",
    "scripting"
  ],
  "host_permissions": [
    "ws://localhost:8000/*",
    "http://localhost:8000/*",
    "http://localhost:5173/*"
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
EOL

# Actualizar webpack.config.js para incluir content.ts
echo -e "${GREEN}[+] Updating webpack.config.js...${NC}"
cat > "$EXT_DIR/webpack.config.js" << 'EOL'
const path = require('path');

module.exports = {
  entry: {
    background: './src/background.ts',
    popup: './src/popup.ts',
    content: './src/content.ts'
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].js'
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js']
  },
  mode: 'development',
  devtool: 'source-map'
};
EOL

# Recompilar la extensión
echo -e "${GREEN}[+] Rebuilding extension...${NC}"
cd "$EXT_DIR"
npx webpack

echo -e "${BLUE}[*] Done! Please reload the extension in your browser.${NC}"
echo -e "${BLUE}[*] If you see any errors, run 'npx webpack' in the extension directory.${NC}"
