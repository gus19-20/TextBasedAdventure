import random
import math
import time
import os
import sys
from TBAfunctions import textManip
import Characters
import Objects
import Rooms


def main():
    newTool = Objects.tool("Sammy", "Is a man", True, 1000000, "Man")
    textManip.clearScreen()
    room1 = Rooms.room(Rooms.event("WibblyWobbly"))   
    textManip.TWprint(room1.EventActivate(), 1)

if __name__ == "__main__":
    main() 