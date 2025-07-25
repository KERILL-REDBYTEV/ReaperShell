#!/bin/bash
# drsearch.sh - ReaperShell Website Directory & File Scanner
# Author: KERILL-REDBYTEV
# For educational use only

clear
echo "====================================="
echo "   ReaperShell - Directory Scanner"
echo "====================================="

# Check if curl exists
if ! command -v curl &>/dev/null; then
    echo "[!] curl not found! Installing..."
    pkg install curl -y
fi

# Target input
read -p "Enter target URL (e.g., http://example.com): " target
target=$(echo "$target" | sed 's:/*$::')  # Remove trailing slash

# Wordlist
read -p "Enter path to wordlist (default: common.txt): " wordlist
wordlist=${wordlist:-wordlists/common.txt}

# Check if wordlist exists
if [ ! -f "$wordlist" ]; then
    echo "[!] Wordlist not found: $wordlist"
    exit 1
fi

# Scan
echo -e "\n[*] Starting directory scan on: $target"
echo "[*] Using wordlist: $wordlist"
echo "[*] Scanning..."

while read path; do
    full="$target/$path"
    response=$(curl -s -o /dev/null -w "%{http_code}" "$full")

    if [[ "$response" == "200" || "$response" == "301" || "$response" == "302" ]]; then
        echo "[+] Found: $full [$response]"
    fi
done < "$wordlist"

echo -e "\n[✓] Scan complete."
read -p "Press ENTER to return to menu..."