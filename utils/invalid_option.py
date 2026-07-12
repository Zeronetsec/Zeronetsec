# https://github.com/Zeronetsec/Zeronetsec

import sys
from utils.color import Color

class InvalidOption:
    @staticmethod
    def execute(args):
        print(f"{Color.R}[!] {Color.N}Invalid option: {Color.GG}{args}{Color.N}")
        print(f"{Color.R}[!] {Color.N}Try: {Color.GG}zeronetsec --help{Color.N}")
        sys.exit(1)

# Copyright (c) 2026 Zeronetsec