#Pushpita Rahman
#Marina DiGregorio
#CS 172-062
#Lab 7

class Room:
    #Constructor sets the description
    #All four doors should be set to None to start
    def __init__(self,descr):
        #Description of the room to print out
        #These should be unique so the player knows where they are
        self.__descr = descr
        #These either tell us what room we get to if we go through the door
        #or they are None if the "door" can't be taken.
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None
    #Access
    #Return the correct values
    def __str__(self):
        return '{}'.format(self.__descr)
    def getNorth(self):
        return self.__north
    def getSouth(self):
        return self.__south
    def getEast(self):
        return self.__east
    def getWest(self):
        return self.__west
        
    #Mutators
    #Update the values
    def setDescription(self,d):
        self.__descr = d
        return self.__descr
    def setNorth(self,n):
        self.__north = n
        return self.__north
    def setSouth(self,s):
        self.__south = s
        return self.__south
    def setEast(self,e):
        self.__east = e
        return self.__east
    def setWest(self,w):
        self.__west = w
        return self.__west
