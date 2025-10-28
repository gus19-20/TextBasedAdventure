from TBAfunctions import textManip
import Objects

class event:
    def __init__(self, eventText):
        self.eventText = eventText
        self.objects = [Objects.object("Mouse Trap", "This is a mousetrap", False)]
    def GetText(self):
        return self.eventText

class room:
    def __init__(self, roomEvent):
        self.textArray = []
        self.eventArray = {"Test":event("This is an event")}
    
    def EventActivate(self):
        textManip.TWprint(self.eventArray.get("Test").GetText(), 1)
        
    
