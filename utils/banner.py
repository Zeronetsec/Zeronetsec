# https://github.com/Zeronetsec/Zeronetsec

import os
import sys
from utils.color import Color

class Banner:
    @staticmethod
    def execute(*args):
        current_dir = os.path.dirname(
            os.path.abspath(__file__),
        )

        file_path = os.path.abspath(
            os.path.join(
                current_dir,
                "..",
                "data",
                "banner.txt",
            ),
        )

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"{Color.B}{content}{Color.N}")
        else:
            print(f"{Color.R}[!] {Color.N}File: {Color.GG}{file_path} {Color.N}not found!")
            sys.exit(1)

# Copyright (c) 2026 Zeronetsec