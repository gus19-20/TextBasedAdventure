import time
import os
import sys
import keyboard

str = ""
class textManip:
    def clearLine():
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

    def clearScreen():
        os.system('cls')

    def threeDot(erase):
        if erase:
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
            if keyboard.is_pressed('q'):
                slow = .001
        print()
