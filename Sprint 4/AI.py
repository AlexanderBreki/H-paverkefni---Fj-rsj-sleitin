class AI():
    def __init__(self, name):
        self.name = name # String
    def getName(self):
        return self.name

class Nonni(Thing):
    def __init__(self):
        self.name = 'Nonni'
        self.msg = 'Fyrir framan Nonna er fjöldi tómra glasa, hann umlar örlítið þegar þú ávarpar hann, þegar þú stjakar við honum snýr hann sér við og þú sérð að hann er mjög fullur. Hann segist geta hjálpað þér ef þú svarar einni spurningu.'
        self.question = 'Hver er munurinn á viskí og koníaki?'
        super(Nonni, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return '0' + self.msg

class Kristjan(Thing):
    def __init__(self):
        self.name = 'Kristján'
        self.msg = 'setja skilaboð hér'
        super(Kristjan, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return self.msg

class Villimadur(Thing):
    def __init__(self):
        self.name = 'villimaður'
        self.msg = 'setja skilaboð hér'
        super(Villimadur, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return self.msg
