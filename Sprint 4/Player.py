import Room

class Player():
    def __init__(self):
        self.lifes = 3
        self.hungover = True
        self.key = False
        self.shell = False
        self.map = False
        self.location = Room.Cabin()

    # Fall sem tekur eitt líf að leikmanni
    def loseLife(self):
        self.lifes -= 1

    # Fall sem gefur leikmanni eitt líf
    def getLife(self):
        self.lifes += 1

    # Fall sem athugar hvort leikmaður sé á lífi
    def isDead(self):
        if (self.lifes <= 0): return True
        return False

    # Fall sem breytir staðsetningu leikmanns
    def changeroom(self, nextroom):
        print (nextroom + " test1")
        if nextroom == 'Skógur':
            if self.map:
                self.location = Room.Forrest()
                return self.location.whereami()
        if nextroom == 'Káeta':
            self.location = Room.Cabin()
            return self.location.whereami()
        elif nextroom == 'Bar':
            self.location = Room.Bar()
            return self.location.whereami()
        elif nextroom == 'Strönd':
            self.location = Room.Beach()
            return self.location.whereami()
        else:
            return '\nÞetta er ekki lögleg staðseting\n'
