# https://github.com/Zeronetsec/Zeronetsec

from utils.color import Color

class Version:
    @staticmethod
    def execute(*args):
        name = "Zeronetsec"
        version = "v0.1"
        creator = "Zeronetsec"
        homepage = "https://github.com/Zeronetsec/Zeronetsec"

        print(f"{Color.N}Name: {Color.GG}{name}{Color.N}")
        print(f"{Color.N}Version: {Color.GG}{version}{Color.N}")
        print(f"{Color.N}Creator: {Color.GG}{creator}{Color.N}")
        print(f"{Color.N}Homepage: {Color.GG}{homepage}{Color.N}")

# Copyright (c) 2026 Zeronetsec