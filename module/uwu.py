# https://github.com/Zeronetsec/Zeronetsec

import time
import sys

class Uwu:
    @staticmethod
    def execute(*args):
        faces = [
            "(｡◕‿◕｡)",
            "(≧◡≦)",
            "ʕ•ᴥ•ʔ",
            "(・ω・)",
            "(๑˃ᴗ˂)ﻭ",
            "(ง'̀-'́)ง",
            "(=^･ω･^=)",
        ]

        delay = 0.2
        duration = 5

        start_time = time.monotonic()
        sys.stdout.write("\x1b[?25l")
        sys.stdout.flush()

        try:
            while (time.monotonic() - start_time) < duration:
                for face in faces:
                    elapsed = time.monotonic() - start_time
                    if elapsed >= duration:
                        break
                    sys.stdout.write(f"\r{face}\x1b[K")
                    sys.stdout.flush()
                    time.sleep(delay)
        finally:
            sys.stdout.write("\x1b[?25h")
            sys.stdout.write("\n")
            sys.stdout.flush()

# Copyright (c) 2026 Zeronetsec