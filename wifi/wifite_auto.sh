#!/bin/bash
# ReaperShell - Automated Wifite Launcher (Educational Use Only)
# Author: KERILL-REDBYTEV

# Color setup
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "============================================"
echo "        ReaperShell - WiFite Auto Mode      "
echo "============================================"
echo -e "${NC}"

# Check if wifite is installed
if ! command -v wifite &> /dev/null; then
    echo -e "${RED}[!] Wifite is not installed! Install it using:${NC}"
    echo -e "${YELLOW}    pkg install wifite${NC}"
    exit 1
fi

# Check for root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}[!] Please run as root or with sudo.${NC}"
    exit 1
fi

# Optional monitor mode enable (for Termux/Nethunter)
echo -e "${GREEN}[*] Enabling monitor mode...${NC}"
ifconfig wlan0 down
iwconfig wlan0 mode monitor
ifconfig wlan0 up

sleep 1

# Start Wifite with selected educational options
echo -e "${GREEN}[*] Starting Wifite...${NC}"
wifite -i wlan0mon --kill --no-wps --dict /usr/share/wordlists/rockyou.txt

# Reminder message
echo -e "${YELLOW}\n[!] Use this only in your own network for testing and education.${NC}"