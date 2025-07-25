#!/bin/bash
# modules/network/nmap_scan.sh - Simple network scanner using nmap
# Author: KERILL-REDBYTEV
# For educational purposes only

clear
echo "=============================="
echo "    ReaperShell - Nmap Scan"
echo "=============================="
echo

# Check if nmap is installed
if ! command -v nmap &> /dev/null; then
    echo "[!] nmap is not installed."
    echo "Install it with: pkg install nmap"
    exit 1
fi

# Prompt for target
read -rp "Enter target IP, subnet, or domain to scan: " target

if [[ -z "$target" ]]; then
    echo "[!] No target provided. Exiting."
    exit 1
fi

echo
echo "[*] Running a basic SYN scan on $target..."
nmap -sS -Pn "$target"

echo
read -rp "Do you want to perform an aggressive scan? (y/n): " choice
if [[ "$choice" =~ ^[Yy]$ ]]; then
    echo "[*] Running aggressive scan on $target (may take time)..."
    nmap -A -v "$target"
fi

echo
echo "Scan completed."
read -rp "Press ENTER to return to the main menu."