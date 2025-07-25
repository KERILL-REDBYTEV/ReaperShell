#!/usr/bin/env python3
"""
core/menu.py - ReaperShell interactive menu
Author: KERILL-REDBYTEV
For educational purposes only
"""

from rich.console import Console
from rich.panel import Panel

console = Console()

def display_banner():
    banner_text = r"""
██████╗ ███████╗ █████╗ ██████╗ ███████╗███████╗██╗  ██╗██╗██╗     ██╗     
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║  ██║██║██║     ██║     
██████╔╝█████╗  ███████║██████╔╝█████╗  ███████╗███████║██║██║     ██║     
██╔═══╝ ██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ╚════██║██╔══██║██║██║     ██║     
██║     ███████╗██║  ██║██║     ███████╗███████║██║  ██║██║███████╗███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
"""
    console.print(Panel.fit(banner_text, title="[red]ReaperShell[/red]", subtitle="By KERILL-REDBYTEV"))

def display_menu():
    """
    Shows the main menu options.
    """
    console.clear()
    display_banner()
    console.print("[bold cyan]Select an option below:[/bold cyan]\n")
    console.print("[bold green]1.[/bold green] Network Scanning")
    console.print("[bold green]2.[/bold green] Web Exploitation")
    console.print("[bold green]3.[/bold green] WiFi Tools")
    console.print("[bold green]4.[/bold green] Bruteforce Attacks")
    console.print("[bold green]5.[/bold green] Denial of Service (DoS)")
    console.print("[bold green]6.[/bold green] Update ReaperShell")
    console.print("[bold red]0.[/bold red] Exit")

def get_choice():
    """
    Get input from user and return it.
    """
    return input("\n[?] Enter your choice: ").strip()

def pause():
    """
    Pauses the script until user presses ENTER.
    """
    input("\nPress ENTER to return to menu...")