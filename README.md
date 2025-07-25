# 💀 ReaperShell: Modular Pentesting Toolkit for Termux

> **ReaperShell** is a powerful, modular penetration testing toolkit for **Termux** on Android.  
> Integrates real pentesting tools: network scanning, web exploitation, WiFi attacks, brute forcing, DoS, and more — for educational and authorized security testing.

---

<div align="center">
  <img src="https://files.catbox.moe/9rk4i8.mp4" width="320" alt="ReaperShell Hacker Animation"/>
</div>

---

## 🚀 1-Click Termux Installation

> **Copy each command below by clicking the <kbd>Copy</kbd> button!**  
> _Watch the **live SVG hacker animations** for each step. Enjoy the pro vibes!_

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/terminal_update_anim.svg" width="26" valign="middle"/> 1. Update & Upgrade Termux

<div class="copy-container">
  <pre><code id="cmd1">pkg update -y && pkg upgrade -y</code></pre>
  <button onclick="copyToClipboard('cmd1')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/install_packages_anim.svg" width="26" valign="middle"/> 2. Install Essentials

<div class="copy-container">
  <pre><code id="cmd2">pkg install -y git python python2 clang make openssh curl wget nano</code></pre>
  <button onclick="copyToClipboard('cmd2')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/clone_anim.svg" width="26" valign="middle"/> 3. Clone ReaperShell

<div class="copy-container">
  <pre><code id="cmd3">git clone https://github.com/KERILL-REDBYTEV/ReaperShell.git</code></pre>
  <button onclick="copyToClipboard('cmd3')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/folder_anim.svg" width="26" valign="middle"/> 4. Enter Directory

<div class="copy-container">
  <pre><code id="cmd4">cd ReaperShell</code></pre>
  <button onclick="copyToClipboard('cmd4')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/exec_anim.svg" width="26" valign="middle"/> 5. Make Scripts Executable

<div class="copy-container">
  <pre><code id="cmd5">chmod +x install.sh uninstall.sh start.sh</code></pre>
  <button onclick="copyToClipboard('cmd5')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/install_anim.svg" width="26" valign="middle"/> 6. Install Dependencies

<div class="copy-container">
  <pre><code id="cmd6">bash install.sh</code></pre>
  <button onclick="copyToClipboard('cmd6')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/hack_anim.svg" width="26" valign="middle"/> 7. Launch ReaperShell!

<div class="copy-container">
  <pre><code id="cmd7">bash start.sh</code></pre>
  <button onclick="copyToClipboard('cmd7')">📋 Copy</button>
</div>

---

## 🛠️ Extra Useful Termux Commands

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/storage_anim.svg" width="26" valign="middle"/> Grant Storage Permission

<div class="copy-container">
  <pre><code id="cmd8">termux-setup-storage</code></pre>
  <button onclick="copyToClipboard('cmd8')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/python_anim.svg" width="26" valign="middle"/> Run Python 3 Scripts

<div class="copy-container">
  <pre><code id="cmd9">python3 core/main.py</code></pre>
  <button onclick="copyToClipboard('cmd9')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/exit_anim.svg" width="26" valign="middle"/> Exit Termux

<div class="copy-container">
  <pre><code id="cmd10">exit</code></pre>
  <button onclick="copyToClipboard('cmd10')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/restore_anim.svg" width="26" valign="middle"/> Restore Original `.bashrc`

<div class="copy-container">
  <pre><code id="cmd11">cp extras/bashrc_backup ~/.bashrc</code></pre>
  <button onclick="copyToClipboard('cmd11')">📋 Copy</button>
</div>

---

### <img src="https://raw.githubusercontent.com/IceFlowTech/assets/main/style_anim.svg" width="26" valign="middle"/> Apply Termux Styling

<div class="copy-container">
  <pre><code id="cmd12">bash extras/termux-style.sh</code></pre>
  <button onclick="copyToClipboard('cmd12')">📋 Copy</button>
</div>

---

## 🎬 Hacker Animations

<div align="center">
  <img src="https://files.catbox.moe/jmu1bl.mp4" width="90%" alt="Matrix Rain"/>
  <img src="https://files.catbox.moe/9rk4i8.mp4" width="370" alt="Terminal Hack Animation"/>
  <img src="https://files.catbox.moe/9rk4i8.mp4" width="220" alt="Cyber Reaper"/>
</div>

---

## 👾 Pro Tips

- Click <kbd>Copy</kbd> to instantly copy each command, one by one!
- Watch the **REAPERSHELL** for inspiration.
- Use ReaperShell **only for educational and authorized security testing**.
- Make your Termux look awesome with extra styling and configs!

---

<div align="center">
  <img src="https://files.catbox.moe/jmu1bl.mp4" width="300"/>
  <br/><br/>
  <b>⚡ Happy Hacking with ReaperShell! ⚡</b>
</div>

---

<!-- Copy-to-Clipboard Script (for GitHub Pages/Markdown renderers that support JS) -->
<script>
function copyToClipboard(id) {
  var code = document.getElementById(id).innerText;
  navigator.clipboard.writeText(code);
  alert("Copied: " + code);
}
</script>
