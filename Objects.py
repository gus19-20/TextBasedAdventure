
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
    
class keyitem(object):
    def __init__(self, name, description, equippable):
        super().__init__(name, description, equippable)
        
