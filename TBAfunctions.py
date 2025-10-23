#tbafunc.py
import time
import os
import sys

str = ""
class textManip:
    def clearLine():
        print("\033[A\033[A") 

    def clearScreen():
        os.system('cls')

    def threeDot():
        textManip.clearLine()
        print(".")
        time.sleep(1)
        textManip.clearLine()
        print("..")
        time.sleep(1)
        textManip.clearLine()
        print("...")
        time.sleep(1)

    def TWprint(words, slow):
        for char in words:
            time.sleep(.03 * slow)
            sys.stdout.write(char)
            sys.stdout.flush()
