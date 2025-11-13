from TBAfunctions import textManip
import Objects
import Characters
import random

class event:
    def __init__(self, eventText):
        self.eventText = eventText
        self.objects = []
        self.activated = False
    def GetText(self):
        return self.eventText
    
    def GetObjects(self):
        return self.objects
    
    def ToggleActivated(self):
        self.activated = True
    
    def GetActive(self):
        return self.activated

class room:
    def __init__(self, roomDescription):
        self.textArray = [roomDescription] #element 0 will always be the room description
        self.eventDict = {"Go back" : event()} #holds all the events
        self.nextRooms = [] #holds all the rooms you can go to next
        self.previousRoom = None #holds the previous room
    
    def EnterRoom(self):
        textManip.TWprint(self.textArray[0])
        control = True
        while control:
            for event in self.eventDict():
                print(f"{event}")
    
    def ConnectRooms(self, Room):
        Room = room(Room)
        self.nextRooms.append(room)
        room.previousRoom = self

    def AddEvent(self, Event, eventName):
        Event = event(Event)
        self.eventDict[eventName] = Event

    def EventActivate(self, player, Event):
        Event = event(Event)
        player = Characters.playerCharacter(player)
        if Event.GetActive() == False:
            textManip.TWprint(Event.GetText(), 1)
            if event.objects.__sizeof__ > 0:
                player.addInv(random.choice(event.GetObjects()))
        else:
            textManip.TWprint("There is nothing more to be done", 1)

startingRoom = room("")

    