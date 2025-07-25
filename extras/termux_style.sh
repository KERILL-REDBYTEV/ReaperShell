#!/bin/bash

# ReaperShell Termux Style Script
# Author: KERILL-REDBYTEV

echo -e "\e[92m[+] Applying Termux visual styles...\e[0m"

# Check for termux-api
if ! command -v termux-reload-settings &> /dev/null; then
    echo -e "\e[91m[!] termux-api not installed. Installing...\e[0m"
    pkg install -y termux-api
fi

# Set default font and color scheme
STORAGE="$HOME/.termux"
mkdir -p "$STORAGE"

# Set font (you can replace with any *.ttf you prefer)
FONT_URL="https://raw.githubusercontent.com/adi1090x/termux-style/master/fonts/JetBrainsMono-Regular.ttf"
wget -qO "$STORAGE/font.ttf" "$FONT_URL"

# Set colors (ReaperShell theme: dark with green text)
cat > "$STORAGE/colors.properties" <<EOF
foreground=#00FF00
background=#000000
color0=#000000
color1=#FF5555
color2=#50FA7B
color3=#F1FA8C
color4=#BD93F9
color5=#FF79C6
color6=#8BE9FD
color7=#BFBFBF
color8=#4D4D4D
color9=#FF6E67
color10=#5AF78E
color11=#F4F99D
color12=#CAA9FA
color13=#FF92D0
color14=#9AEDFE
color15=#E6E6E6
EOF

termux-reload-settings
echo -e "\e[92m[+] Termux style applied!\e[0m"