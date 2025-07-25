#!/usr/bin/env python3
"""
core/updater.py - Updates ReaperShell from its GitHub repo
Author: KERILL-REDBYTEV
For educational purposes only
"""

import os
import sys
from time import sleep
from rich.console import Console

console = Console()

# Set your official GitHub repo URL here:
GITHUB_REPO = "https://github.com/KERILL-REDBYTEV/ReaperShell.git"
REAPER_DIR = os.path.expanduser("~/ReaperShell")

def git_pull():
    if not os.path.isdir(REAPER_DIR):
        console.print(f"[bold red]Error:[/bold red] ReaperShell directory not found at {REAPER_DIR}")
        console.print("Please install the tool first.")
        sys.exit(1)

    os.chdir(REAPER_DIR)
    console.print("[*] Fetching latest updates from GitHub...")
    result = os.system("git pull origin main")

    if result == 0:
        console.print("[bold green]Update successful![/bold green]")
    else:
        console.print("[bold red]Failed to update ReaperShell. Please check your network or git setup.[/bold red]")

def main():
    try:
        git_pull()
    except KeyboardInterrupt:
        console.print("\n[bold red]Update interrupted by user.[/bold red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Unexpected error:[/bold red] {e}")
        sys.exit(1)
    sleep(2)

if __name__ == "__main__":
    main()