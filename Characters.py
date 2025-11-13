from TBAfunctions import textManip
import Objects

class Character:
    def __init__(self, health):
        self.health = health
        self.inventory = Objects.object([])
        self.tool = Objects.object("N/A", "N/A", False)
    

class playerCharacter:
    def __init__(self):
        self.health = 100
        self.maxInv = 5
        self.inventory = []
        self.tool = Objects.tool("N/A", "N/A", False, 0, "N/A")
        self.hand = Objects.object("N/A", "N/A", False)
    
    def checkInvFull(self):
        if self.inventory.__sizeof__() == self.maxInv:
            return True

    def addInv(self, obj):
        if not playerCharacter.checkInvFull(self):
            self.inventory.append(obj)
        else:
            textManip.TWprint("Your inventory is full", 1)
    
    def removeInv(self, element):
        self.inventory.pop(element)
    
    def changeHealth(self, num):
        self.health = self.health + num

    def changeTool(self, tool):
        self.tool = tool
    
    def InspectTool(self):
        if self.tool.name != "N/A":
            return f"Name: {self.tool.GetName()}\nType: {self.tool.GetToolType()}\nDamage: {self.tool.GetDamage()}\nDescription: {self.tool.GetDesc()}"
        else:
            return "No tool equipped"
    
    def InspectInv(self):
        for item in self.inventory:
            print("-------------------", 1)
            item.GetDeets()
        print("-------------------", 1)