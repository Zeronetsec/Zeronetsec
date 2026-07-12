# https://github.com/Zeronetsec/Zeronetsec

import os
import subprocess
import sys
from utils.color import Color

class Readme:
    @staticmethod
    def execute(*args):
        current_dir = os.path.dirname(
            os.path.abspath(__file__),
        )

        readme_path = os.path.abspath(
            os.path.join(current_dir, "..", "README.md"),
        )

        if not os.path.exists(readme_path):
            print(f"{Color.R}[!] {Color.N}File: {Color.GG}{readme_path} {Color.N}not found!")
            sys.exit(1)

        try:
            subprocess.run(
                ["glow", readme_path],
                check=True,
            )
        except FileNotFoundError:
            print(f"{Color.R}[!] {Color.N}Command: {Color.GG}glow {Color.N}not found!", file=sys.stderr)
            sys.exit(1)
        except subprocess.CalledProcessError:
            print(f"{Color.R}[!] {Color.N}Failed showing: {Color.GG}README.md{Color.N}", file=sys.stderr)
            sys.exit(1)

# Copyright (c) 2026 Zeronetsec