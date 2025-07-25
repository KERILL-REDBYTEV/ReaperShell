#!/usr/bin/env python3
"""
core/main.py - ReaperShell entry point
Author: KERILL-REDBYTEV
Educational use only
"""

import os
import sys
import time
import datetime
from core import menu
from core.auth import authenticate

LOG_FILE = "logs/reapershell.log"

def log_event(event: str):
    """
    Append an event to the log file with timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = os.getenv("USER") or os.getenv("USERNAME") or "unknown"
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] ({user}) {event}\n")

def run_network_menu():
    os.system("bash modules/network/nmap_scan.sh")

def run_ip_sweep():
    os.system("python3 modules/network/ip_sweep.py")

def update_shell():
    os.system("python3 core/updater.py")

def main():
    if not authenticate():
        print("[!] Authentication failed. Exiting.")
        sys.exit(1)

    log_event("User logged into ReaperShell")

    while True:
        try:
            menu.display_menu()
            choice = menu.get_choice()

            if choice == "1":
                run_network_menu()
            elif choice == "2":
                print("[*] Web exploitation tools coming soon.")
                menu.pause()
            elif choice == "3":
                print("[*] WiFi tools module coming soon.")
                menu.pause()
            elif choice == "4":
                print("[*] Bruteforce attacks module coming soon.")
                menu.pause()
            elif choice == "5":
                print("[*] DoS tools coming soon.")
                menu.pause()
            elif choice == "6":
                update_shell()
            elif choice == "0":
                print("\n[!] Exiting ReaperShell.")
                log_event("User exited ReaperShell\n")
                break
            else:
                print("[!] Invalid choice.")
                menu.pause()

        except KeyboardInterrupt:
            print("\n[!] Interrupted by user.")
            log_event("User interrupted ReaperShell\n")
            break

if __name__ == "__main__":
    main()