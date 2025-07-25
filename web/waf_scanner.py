#!/usr/bin/env python3
# waf_scanner.py - ReaperShell WAF Detector
# Author: KERILL-REDBYTEV
# Educational use only

import requests
import sys

WAF_SIGNATURES = {
    "cloudflare": ["cloudflare", "cf-ray", "__cfduid"],
    "sucuri": ["sucuri", "x-sucuri"],
    "imperva": ["incapsula", "x-iinfo", "visid_incap"],
    "aws": ["aws-alb", "x-amz"],
    "akamai": ["akamai", "akamai-bot"],
    "barracuda": ["barracuda", "barracudawaf"],
    "dosenet": ["dotdefender"],
    "mod_security": ["mod_security", "modsecurity"],
    "f5_big_ip": ["bigip", "x-waf", "f5"],
    "radware": ["radware", "alkacon"],
    "360wzb": ["wzws", "wzws-rid"]
}

def detect_waf(url: str):
    print(f"\n[*] Sending test request to {url}...")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; ReaperShellScanner/1.0)",
            "X-Forwarded-For": "127.0.0.1",
            "X-Originating-IP": "127.0.0.1",
            "X-Remote-IP": "127.0.0.1",
            "X-Remote-Addr": "127.0.0.1"
        }
        response = requests.get(url, headers=headers, timeout=10)

        print("[*] Response received. Analyzing headers...\n")
        detected = []

        for waf, signatures in WAF_SIGNATURES.items():
            for header, value in response.headers.items():
                for sig in signatures:
                    if sig.lower() in header.lower() or sig.lower() in value.lower():
                        detected.append(waf)
                        break

        if detected:
            print(f"[+] WAF Detected: {', '.join(set(detected)).title()}")
        else:
            print("[-] No known WAF detected.")

    except requests.exceptions.RequestException as e:
        print(f"[!] Request failed: {e}")

def main():
    print("=======================================")
    print("     ReaperShell - WAF Scanner")
    print("=======================================\n")

    target = input("Enter target URL (e.g., https://example.com): ").strip()
    if not target.startswith("http"):
        target = "http://" + target

    detect_waf(target)

    input("\n[+] Press ENTER to return to menu...")

if __name__ == "__main__":
    main()