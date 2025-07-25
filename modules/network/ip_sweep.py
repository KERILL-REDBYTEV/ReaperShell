#!/usr/bin/env python3
"""
modules/network/ip_sweep.py - Fast ICMP-based IP sweep tool
Author: KERILL-REDBYTEV
For educational purposes only
"""

import ipaddress
import platform
import subprocess
import threading
from queue import Queue
from rich.console import Console

console = Console()
queue = Queue()
active_hosts = []

# Detect ping command style
param = "-n" if platform.system().lower() == "windows" else "-c"

def ping_host(ip):
    try:
        output = subprocess.run(
            ["ping", param, "1", str(ip)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if output.returncode == 0:
            console.print(f"[green][+] Active:[/green] {ip}")
            active_hosts.append(str(ip))
    except Exception:
        pass

def worker():
    while not queue.empty():
        ip = queue.get()
        ping_host(ip)
        queue.task_done()

def main():
    console.print("[bold cyan]ReaperShell - IP Sweep Tool[/bold cyan]\n")
    subnet_input = input("Enter subnet (e.g. 192.168.1.0/24): ").strip()

    try:
        ip_net = ipaddress.ip_network(subnet_input, strict=False)
    except ValueError:
        console.print("[red]Invalid subnet! Use format: 192.168.1.0/24[/red]")
        return

    for ip in ip_net.hosts():
        queue.put(ip)

    console.print(f"[yellow][*] Scanning {queue.qsize()} hosts...[/yellow]\n")

    thread_count = 50
    threads = []

    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.daemon = True
        threads.append(t)
        t.start()

    queue.join()

    console.print(f"\n[bold green]Scan complete! {len(active_hosts)} hosts are up.[/bold green]")

    if active_hosts:
        for host in active_hosts:
            console.print(f"[cyan]  ↪ {host}[/cyan]")

    input("\nPress ENTER to return to menu...")

if __name__ == "__main__":
    main()