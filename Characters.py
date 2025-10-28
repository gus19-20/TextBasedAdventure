from TBAfunctions import textManip
import Objects

class Character:
    def __init__(self, health):
        self.health = health
        self.inventory = []
        self.tool = Objects.tool("N/A", "N/A", "N/A", 0)

class playerCharacter:
    def __init__(self):
        self.health = 100
        self.maxInv = 5
        self.inventory = []
        self.tool = Objects.tool("N/A", "N/A", "N/A", 0)
        self.hand = Objects.object("N/A", "N/A")
    
    def checkInvFull(self):
        if self.inventory.__sizeof__() == self.maxInv:
            return True

    def addInv(self, obj):
        if not playerCharacter.checkInvFull(self):
            self.inventory.append(obj)
        else:
            textManip.TWprint("Your inventory is full", 1)
    
    def changeHealth(self, num):
        self.health = self.health + num

    def changeTool(self, tool):
        self.tool = tool
    
    def InspectTool(self):
        if self.tool.name != "N/A":
            return f"Name: {self.tool.GetName()}\nType: {self.tool.GetToolType()}\nDamage: {self.tool.GetDamage()}\nDescription: {self.tool.GetDesc()}"
        else:
            return "No tool equipped"
