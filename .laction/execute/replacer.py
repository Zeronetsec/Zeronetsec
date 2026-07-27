#!/usr/bin/env python3

import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
project_root = ROOT_DIR.parent.parent

readme_path = project_root / "README.md"

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
        print(f"\x1b[0;32m[+] \x1b[0mChanged: \x1b[0;32m{old_url} \x1b[1;90m-> \x1b[0;32m{new_path}\x1b[0m")
    else:
        print(f"\x1b[0;33m[!] \x1b[0mTarget URL: \x1b[0;32m{old_url} \x1b[0mnot found!")

except FileNotFoundError:
    print(f"\x1b[1;31m[!] \x1b[0mFile: \x1b[0;32m{os.path.abspath(readme_path)} \x1b[0mnot found!")
    sys.exit(1)