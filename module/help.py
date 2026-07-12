# https://github.com/Zeronetsec/Zeronetsec

import os
import glob
import json
import sys
from utils.color import Color
from utils.banner import Banner
from utils.birthday import Birthday

class Help:
    @staticmethod
    def execute(*args):
        Banner.execute()
        Birthday.execute()

        print(f"{Color.N}Usage: {Color.GG}zeronetsec {Color.CC}<option> [<args>]{Color.N}")
        print()
        print(f"{Color.N}Available options:")

        current_dir = os.path.dirname(
            os.path.abspath(__file__),
        )

        metadata_dir = os.path.abspath(
            os.path.join(current_dir, "..", "metadata"),
        )

        search_pattern = os.path.join(
            metadata_dir, "*.json",
        )

        files = glob.glob(search_pattern)
        if not files:
            print(f"{Color.R}[!] {Color.N}Error reading config: {Color.GG}{metadata_dir} {Color.N}no metadata files found!", file=sys.stderr)
            sys.exit(1)

        for f_path in sorted(files):
            try:
                with open(f_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                command = data.get("Command", "")
                description = data.get("Description", "")
                hp_args = data.get("Args", "")

                formatted_args = f" {hp_args}" if hp_args else ""

                print(f"    {Color.DG}* {Color.GG}{command}{Color.CC}{formatted_args}{Color.N}")
                print(f"    {Color.DG}└── {Color.WW}{description}{Color.N}")

            except (json.JSONDecodeError, IOError):
                continue

# Copyright (c) 2026 Zeronetsec