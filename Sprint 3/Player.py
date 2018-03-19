import Room

class Player():
    def __init__(self):
        self.lifes = 3
        self.hungover = True
        self.key = False
        self.earring = False
        self.map = False
        self.location = Room.Cabin()

    # Fall sem tekur eitt líf að leikmanni
    def loseLife(self):
        self.lifes -= 1

    # Fall sem gefur leikmanni eitt líf
    def getLife(self):
        self.lifes += 1

    # Fall sem athugar hvort leikmaður sé á lífi
    def isAlive(self):
        if (self.lifes <= 0): return False
        return True

    # Fall sem breytir staðsetningu leikmanns
    def changeroom(self, nextroom):
        print (nextroom + " test1")
        if nextroom == 'káeta':
            self.location = Room.Cabin()
            return self.location.whereami()
        elif nextroom == 'bar':
            self.location = Room.Bar()
            return self.location.whereami()
        elif nextroom == 'strönd':
            self.location = Room.Beach()
            return self.location.whereami()
        elif nextroom == 'skógur':
            if self.map:
                self.location = Room.Forrest()
                return self.location.whereami()
        else:
            return 'Þetta er ekki lögleg staðseting'
