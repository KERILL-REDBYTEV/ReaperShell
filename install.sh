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

echo -e "\n[+] Starting installation of ReaperShell..."

# Backup .bashrc
cp $HOME/.bashrc $HOME/.bashrc.bak-reapershell

# Add ReaperShell launcher to .bashrc (persistent banner)
if ! grep -q "ReaperShell/start.sh" "$HOME/.bashrc"; then
    echo -e "\n# ReaperShell Auto-Start" >> $HOME/.bashrc
    echo "bash \$HOME/ReaperShell/start.sh" >> $HOME/.bashrc
    echo "[+] ReaperShell auto-start added to .bashrc"
fi

# Update and install dependencies
echo "[+] Installing dependencies..."
pkg update -y && pkg upgrade -y
pkg install -y python git wget curl nmap tsu clang

# Optional tools
pkg install -y hydra openssh termux-api

# Python modules
pip install --upgrade pip
pip install requests colorama rich

# Clone external tools
echo "[+] Cloning external tools..."
mkdir -p tools/external

# SQLMap
if [ ! -d "tools/external/sqlmap" ]; then
    git clone --depth=1 https://github.com/sqlmapproject/sqlmap.git tools/external/sqlmap
fi

# Wifite (will work only on supported devices)
if [ ! -d "tools/external/wifite" ]; then
    git clone --depth=1 https://github.com/derv82/wifite.git tools/external/wifite
fi

# Make start script executable
chmod +x start.sh

# Done
echo -e "\n[✔] ReaperShell installation complete!"
echo -e "[!] Please restart Termux or run: bash start.sh\n"

exit 0