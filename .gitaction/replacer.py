#!/usr/bin/env python3

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
readme_path = os.path.join(script_dir, "..", "README.md")

old_url = "https://raw.githubusercontent.com/Zeronetsec/Zeronetsec/main/.gitaction/github-snake-tokyonight.svg"
new_path = ".gitaction/github-snake-tokyonight.svg"

try:
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    if old_url in content:
        updated_content = content.replace(
            old_url, new_path,
        )
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"[+] Changed: {old_url} -> {new_path}")
    else:
        print(f"[!] Target URL: {old_url} not found!")

except FileNotFoundError:
    print(f"[!] File: {os.path.abspath(readme_path)} not found!")