#!/bin/bash
# monitor_enable.sh - Enable monitor mode on a wireless interface
# Author: KERILL-REDBYTEV
# Educational use only

clear
echo "========================================"
echo "      ReaperShell - Enable Monitor Mode"
echo "========================================"

# Check root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "[!] Please run this script as root or with sudo."
    exit 1
fi

# Check for required tools
if ! command -v airmon-ng &>/dev/null; then
    echo "[!] 'airmon-ng' not found. Installing aircrack-ng package..."
    pkg install aircrack-ng -y
fi

echo "[*] Scanning for wireless interfaces..."

interfaces=$(iwconfig 2>/dev/null | grep "IEEE 802.11" | awk '{print $1}')

if [ -z "$interfaces" ]; then
    echo "[!] No wireless interfaces found."
    exit 1
fi

echo "Available wireless interfaces:"
select iface in $interfaces; do
    if [ -n "$iface" ]; then
        echo "[*] Selected interface: $iface"
        echo "[*] Killing interfering processes..."
        airmon-ng check kill

        echo "[*] Enabling monitor mode on $iface..."
        airmon-ng start "$iface"

        # Check if monitor mode enabled successfully
        monitor_iface="${iface}mon"
        if iwconfig "$monitor_iface" 2>/dev/null | grep -q "Mode:Monitor"; then
            echo "[✓] Monitor mode enabled on interface: $monitor_iface"
        else
            echo "[!] Failed to enable monitor mode on $iface"
        fi
        break
    else
        echo "[!] Invalid selection, please try again."
    fi
done

read -p "Press ENTER to return to the menu..."