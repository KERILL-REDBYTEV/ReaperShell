#!/usr/bin/env python3
"""
core/auth.py - Basic authentication for ReaperShell
Author: KERILL-REDBYTEV
For educational purposes only
"""

import getpass
from rich.console import Console

console = Console()

# Hardcoded credentials (change as needed)
USERNAME = "admin"
PASSWORD = "reapershell2025"

MAX_ATTEMPTS = 3

def authenticate():
    """
    Prompt user for username and password with masking.
    Returns True if credentials match, else False.
    """
    console.print("[bold cyan]Please login to ReaperShell[/bold cyan]")
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        username_input = input("Username: ").strip()
        password_input = getpass.getpass("Password: ")

        if username_input == USERNAME and password_input == PASSWORD:
            console.print("[bold green]Login successful![/bold green]")
            return True
        else:
            attempts += 1
            console.print(f"[bold red]Invalid credentials![/bold red] Attempts left: {MAX_ATTEMPTS - attempts}")

    console.print("[bold red]Maximum login attempts exceeded. Exiting...[/bold red]")
    return False

if __name__ == "__main__":
    if not authenticate():
        exit(1)