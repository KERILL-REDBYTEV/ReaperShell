#!/bin/bash

# ReaperShell Installer Script
# Author: KERILL-REDBYTEV
# For educational use only!

clear

# ASCII Banner
cat << "EOF"

██████  ███████  █████  ██████  ███████ ███████ ██   ██ ██      ██      
██   ██ ██      ██   ██ ██   ██ ██      ██      ██   ██ ██      ██      
██████  █████   ███████ ██████  █████   █████   ███████ ██      ██      
██   ██ ██      ██   ██ ██   ██ ██      ██      ██   ██ ██      ██      
██   ██ ███████ ██   ██ ██   ██ ███████ ███████ ██   ██ ███████ ███████ 
                                                                        

        ⚠️ For Educational Use Only ⚠️
       Unauthorized use is strictly prohibited

EOF

echo -e "\n[+] Starting ReaperShell installation...\n"

# Backup .bashrc if not already backed up
if [ ! -f "$HOME/.bashrc.bak-reapershell" ]; then
    echo "[*] Backing up existing .bashrc to .bashrc.bak-reapershell"
    cp "$HOME/.bashrc" "$HOME/.bashrc.bak-reapershell"
else
    echo "[*] Backup .bashrc.bak-reapershell already exists"
fi

# Append .bashrc_append safely to .bashrc if not present
if ! grep -q "REAPERSHELL AUTO-START" "$HOME/.bashrc"; then
    echo "[*] Adding ReaperShell auto-start to .bashrc"
    cat "$HOME/ReaperShell/.bashrc_append" >> "$HOME/.bashrc"
else
    echo "[*] ReaperShell auto-start already in .bashrc"
fi

# Update packages and install dependencies
echo "[*] Updating packages..."
pkg update -y && pkg upgrade -y

echo "[*] Installing required packages..."
pkg install -y python git wget curl nmap tsu clang hydra openssh termux-api

# Upgrade pip and install Python packages
echo "[*] Installing Python packages..."
pip install --upgrade pip
pip install requests colorama rich

# Create tools/external directory if missing
mkdir -p "$HOME/ReaperShell/tools/external"

# Clone SQLMap if not present
if [ ! -d "$HOME/ReaperShell/tools/external/sqlmap" ]; then
    echo "[*] Cloning SQLMap..."
    git clone --depth=1 https://github.com/sqlmapproject/sqlmap.git "$HOME/ReaperShell/tools/external/sqlmap"
else
    echo "[*] SQLMap already cloned"
fi

# Clone Wifite if not present
if [ ! -d "$HOME/ReaperShell/tools/external/wifite" ]; then
    echo "[*] Cloning Wifite..."
    git clone --depth=1 https://github.com/derv82/wifite.git "$HOME/ReaperShell/tools/external/wifite"
else
    echo "[*] Wifite already cloned"
fi

# Make start.sh executable
if [ -f "$HOME/ReaperShell/start.sh" ]; then
    chmod +x "$HOME/ReaperShell/start.sh"
    echo "[*] start.sh permission set to executable"
else
    echo "[!] start.sh not found, please check your installation."
fi

echo -e "\n[✔] ReaperShell installation completed!"
echo "[!] Restart Termux or run 'bash $HOME/ReaperShell/start.sh' to launch the tool."

exit 0