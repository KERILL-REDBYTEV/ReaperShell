#!/bin/bash

# ReaperShell Uninstaller Script
# Author: KERILL-REDBYTEV
# For educational use only!

clear

# ASCII Title
cat << "EOF"

██████  ███████  █████  ██████  ███████ ███████ ██   ██ ██      ██      
██   ██ ██      ██   ██ ██   ██ ██      ██      ██   ██ ██      ██      
██████  █████   ███████ ██████  █████   █████   ███████ ██      ██      
██   ██ ██      ██   ██ ██   ██ ██      ██      ██   ██ ██      ██      
██   ██ ███████ ██   ██ ██   ██ ███████ ███████ ██   ██ ███████ ███████ 
                                                                        

             ✘ UNINSTALLING ReaperShell ✘

EOF

# Confirm uninstall
read -p "⚠️ Are you sure you want to uninstall ReaperShell? (y/N): " confirm
confirm=${confirm,,} # lowercase

if [[ "$confirm" != "y" && "$confirm" != "yes" ]]; then
    echo "[-] Uninstall cancelled."
    exit 0
fi

# Remove ReaperShell auto-start lines from .bashrc
if grep -q "ReaperShell/start.sh" "$HOME/.bashrc"; then
    echo "[*] Removing auto-start from .bashrc..."
    sed -i '/ReaperShell\/start.sh/d' "$HOME/.bashrc"
    sed -i '/ReaperShell Auto-Start/d' "$HOME/.bashrc"
fi

# Restore backup if available
if [ -f "$HOME/.bashrc.bak-reapershell" ]; then
    echo "[*] Restoring original .bashrc..."
    cp "$HOME/.bashrc.bak-reapershell" "$HOME/.bashrc"
    rm "$HOME/.bashrc.bak-reapershell"
fi

# Delete tool directory
cd "$HOME"
if [ -d "ReaperShell" ]; then
    echo "[*] Deleting ReaperShell directory..."
    rm -rf ReaperShell
fi

echo -e "\n[✔] ReaperShell has been completely uninstalled!"
echo "[!] Restart Termux to see changes."

exit 0