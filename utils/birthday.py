# https://github.com/Zeronetsec/Zeronetsec

from datetime import datetime
from utils.color import Color

class Birthday:
    @staticmethod
    def execute(*args):
        birth_date = "07-13"
        today = datetime.now().strftime("%m-%d")
        
        if today == birth_date:
            print(f"{Color.R}› {Color.N}Happy birthday for {Color.GG}zeronetsec {Color.N}🎉")
            print()

# Copyright (c) 2026 Zeronetsec