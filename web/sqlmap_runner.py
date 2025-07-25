#!/usr/bin/env python3
"""
web/sqlmap_runner.py - SQLMap interface for ReaperShell
Author: KERILL-REDBYTEV
Educational use only
"""

import os
import sys
import subprocess

def check_sqlmap():
    if not shutil.which("sqlmap"):
        print("[!] sqlmap is not installed.")
        print("    Install it with: pkg install sqlmap")
        sys.exit(1)

def run_sqlmap(url: str, dump: bool = False, level: int = 1, risk: int = 1):
    cmd = ["sqlmap", "-u", url, "--batch", f"--level={level}", f"--risk={risk}"]
    
    if dump:
        cmd.append("--dump")

    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[!] Scan aborted.")
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    import shutil
    check_sqlmap()
    
    print("\n===============================")
    print("     ReaperShell - SQLMap")
    print("===============================\n")
    
    target = input("Enter target vulnerable URL: ").strip()
    
    if not target:
        print("[!] No URL provided. Exiting.")
        return

    dump = input("Do you want to dump the database? (y/n): ").lower().startswith('y')
    try:
        level = int(input("Level (1-5) [default 1]: ") or "1")
        risk = int(input("Risk (1-3) [default 1]: ") or "1")
    except ValueError:
        level, risk = 1, 1

    print(f"\n[*] Starting SQLMap scan on: {target}")
    run_sqlmap(target, dump=dump, level=level, risk=risk)

    input("\n[+] Press ENTER to return to menu...")

if __name__ == "__main__":
    main()