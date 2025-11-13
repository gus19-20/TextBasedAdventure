
class object:
    def __init__(self, name, description, equippable):
        self.name = name
        self.description = description
        self.equippable = equippable

    def GetDesc(self):
        return self.description
    
    def GetName(self):
        return self.name
    
    def IsEquippable(self):
        return self.equippable
    
    def PrintDeets(self):
        print(f"{self.GetName()}\n\n{self.GetDesc()}")

class tool(object):
    def __init__(self, name, description, equippable, damage, type):
        super().__init__(name, description, equippable)
        self.damage = damage
        self.type = type
    
    def GetDesc(self):
        return self.description
    
    def GetName(self):
        return self.name

    def GetToolType (self):
        return self.type

    def GetDamage(self):
        return self.damage
    
    def PrintDeets(self):
        print(f"{self.GetName()}\n\n{self.GetDamage()}\n\n{self.GetToolType()}\n\n{self.GetDesc()}")
    
class keyitem(object):
    def __init__(self, name, description, equippable):
        super().__init__(name, description, equippable)


