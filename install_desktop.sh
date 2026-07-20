#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_NAME="PredixAI Robô de Listas"
DESKTOP_FILE_NAME="predixai-robo-de-listas.desktop"
ICON_SOURCE="$ROOT_DIR/assets/logo_predixai.svg"
ICON_DIR="$HOME/.local/share/icons/hicolor/scalable/apps"
APPLICATIONS_DIR="$HOME/.local/share/applications"

chmod +x "$ROOT_DIR/run.sh" "$ROOT_DIR/install.sh" "$ROOT_DIR/install_desktop.sh" 2>/dev/null || true

if [[ ! -f "$ICON_SOURCE" ]]; then
  echo "Logo não encontrada: $ICON_SOURCE" >&2
  exit 1
fi

mkdir -p "$ICON_DIR" "$APPLICATIONS_DIR"
cp "$ICON_SOURCE" "$ICON_DIR/predixai-robo-de-listas.svg"

DESKTOP_CONTENT="[Desktop Entry]
Type=Application
Version=1.0
Name=$APP_NAME
Comment=Perfis, listas datadas e execução controlada
Exec=/usr/bin/env bash $ROOT_DIR/run.sh
Icon=$ICON_DIR/predixai-robo-de-listas.svg
Path=$ROOT_DIR
Terminal=false
Categories=Utility;
StartupNotify=true
"

printf '%s' "$DESKTOP_CONTENT" > "$APPLICATIONS_DIR/$DESKTOP_FILE_NAME"
chmod +x "$APPLICATIONS_DIR/$DESKTOP_FILE_NAME"

DESKTOP_DIR=""
if command -v xdg-user-dir >/dev/null 2>&1; then
  DESKTOP_DIR="$(xdg-user-dir DESKTOP 2>/dev/null || true)"
fi

if [[ -z "$DESKTOP_DIR" || "$DESKTOP_DIR" == "$HOME" ]]; then
  for candidate in "$HOME/Área de Trabalho" "$HOME/Desktop"; do
    if [[ -d "$candidate" ]]; then
      DESKTOP_DIR="$candidate"
      break
    fi
  done
fi

if [[ -n "$DESKTOP_DIR" && -d "$DESKTOP_DIR" ]]; then
  cp "$APPLICATIONS_DIR/$DESKTOP_FILE_NAME" "$DESKTOP_DIR/$DESKTOP_FILE_NAME"
  chmod +x "$DESKTOP_DIR/$DESKTOP_FILE_NAME"
  echo "Atalho criado em: $DESKTOP_DIR/$DESKTOP_FILE_NAME"
else
  echo "Atalho instalado no menu de aplicativos: $APPLICATIONS_DIR/$DESKTOP_FILE_NAME"
  echo "A pasta da área de trabalho não foi localizada automaticamente."
fi

echo "$APP_NAME instalado com sucesso."
