#!/usr/bin/env python3
"""
modules/network/traceroute.py - Custom Traceroute Tool
Author: KERILL-REDBYTEV
Educational use only
"""

import sys
import time
from scapy.all import IP, ICMP, sr1, conf

def traceroute(dest_name, max_hops=30, timeout=2):
    print(f"\n[*] Tracing route to {dest_name} over {max_hops} hops:\n")

    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=dest_name, ttl=ttl) / ICMP()
        start_time = time.time()
        reply = sr1(pkt, verbose=0, timeout=timeout)
        rtt = round((time.time() - start_time) * 1000)

        if reply is None:
            print(f"{ttl:2}   *   Request timed out")
        elif reply.type == 0:
            print(f"{ttl:2}   {reply.src}   {rtt} ms (destination reached)")
            break
        else:
            print(f"{ttl:2}   {reply.src}   {rtt} ms")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 traceroute.py <target>")
        sys.exit(1)

    target = sys.argv[1]
    try:
        traceroute(target)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    conf.verb = 0  # Disable scapy verbose output globally
    main()