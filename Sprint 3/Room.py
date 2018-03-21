import Thing

class Room():
    def __init__(self, name, hidden):
        self.name = name # String
        self.hidden = hidden # Boolean

    def getName(self):
        return self.name
    def isHidden(self):
        if self.Hidden: return True
        return False
    def WhatsHere(self): pass
    def wherecanigo(self): pass

class Cabin(Room):
    def __init__(self):
        self.name = 'Káeta'
        self.things = ['skápur', 'skrifborð', 'rúm']
        self.locker = Thing.Locker()
        self.desk = Thing.Desk()
        self.bed = Thing.Bed()
        self.description = """
Þú ert í káetunni. Hún er lítil og dimm og loftið er þungt.
Eina ljósið í herberginu er sólarljósið sem skín í gegnum götótt
gluggatjöldin. Þú horfir í kringum þig. Í einu horninu er lítið
<rúm> og við enda þess er gamalt <skrifborð> með skúffu. Í hinum
enda herbergisins er <skápur>.
        """
        self.hidden = False
        super(Cabin, self).__init__(self.name, self.hidden)

    def whatshere(self):
        whatshere = ''
        for i in self.things:
            whatshere += '<' + i + '> '
        return whatshere

    def whereami(self):
        return self.description

    def wherecanigo(self, map):
        if map:
            return '<bar> <strönd> <skógur>'
        else:
            return '<bar> <strönd>'

    def interact(self, thing, hungover, key, earring, map):
        if thing == 'skápur':
            return self.locker.interact(thing, hungover, key, earring, map)
        elif thing == 'skrifborð':
            return self.desk.interact(thing, hungover, key, earring, map)
        elif thing == 'rúm':
            return self.bed.interact(thing, hungover, key, earring, map)
        else:
            return 'Þessi hlutur er ekki hér'

class Bar(Room):
    def __init__(self):
        self.name = 'Bar'
        self.things = ['Nonni', 'barþjónn', 'Jósefína', 'Einar']
        self.hidden = False
        self.bartender = Thing.Bartender()
        self.nonni = Thing.Nonni()
        self.josefina = Thing.Josefina()
        self.einar = Thing.Einar()
        self.description = """"
Þú ert á barnum. Hann er ekki stór, varla nema lítill kofi við bryggjuna.
Innan við er sterkur tóbaksfnykur. Við barinn stendur <barþjónn>, stór
svertingi frá Kúbu, og raðar flöskum í hillur. Nokkrir gestir eru á barnum,
við barborðið situr <Nonni> sjóræningi sem þú þekkir ágætlega, þig rámar
óljóst í að þú hafir hitt hann í gærkvöldi. Í dimmu horni situr
<Einar gamli> og skrifar í bók. Framarlega í herberginu situr
<Fröken Jósefína>, óskilgetin dóttir landsstjóra eyjunnar, við borð og
drekkur úr vínglasi ásamt öðrum konum.
         """
        super(Bar, self).__init__(self.name, self.hidden)

    def whatshere(self):
        whatshere = ''
        for i in self.things:
            whatshere += '<' + i + '> '
        return whatshere

    def whereami(self):
        return self.description

    def wherecanigo(self, map):
        if map:
            return '<Káeta> <Strönd> <skógur>'
        else:
            return '<Káeta> <Strönd>'

    def interact(self, thing, hungover, key, earring, map):
        if thing == 'barþjónn':
            return self.bartender.interact(thing, hungover, key, earring, map)
        elif thing == 'Nonni':
            return self.nonni.interact(thing, hungover, key, earring, map)
        elif thing == 'Jósefína':
            return self.josefina.interact(thing, hungover, key, earring, map)
        elif thing == 'Einar':
            return self.einar.interact(thing, hungover, key, earring, map)
        else:
            return 'Þessi hlutur er ekki hér'

class Beach(Room):
    def __init__(self):
        self.name = 'Strönd'
        self.things = ['Kristján', 'kona', 'skúr']
        self.kristjan = Things.Kristjan()
        self.kona = Thing.Kona()
        self.skur = Thing.Skur()
        self.description = """
Þú ert á ströndinni. Það er gott veður úti og sjórinn er lygn. Í fjörunni
gengur ljóshærð <kona> og horfir út á sjóinn. Á ströndinni kemur þú auga á
hóp katta, þegar þú nálgast þá sérðu tötraralegan mann liggja í miðjum
kattahópnum með undarlega hliðartösku slengda um aðra öxlina, það er
<Kristján> róni.
        """
        self.hidden = False
        super(Beach, self).__init__(self.name, self.hidden)

    def whatshere(self):
        return self.things

    def whereami(self):
        return self.description

    def wherecanigo(self, map):
        if map:
            return '<káeta> <bar> <skógur>'
        else:
            return '<káeta> <bar>'

    def interact(self, thing, hungover, key, earring, map):
        if thing == 'Kristján':
            return self.kristjan.interact(thing, hungover, key, earring, map)
        elif thing == 'kona':
            return self.kona.interact(thing, hungover, key, earring, map)
        elif thing == 'skúr':
            return self.skur.interact(thing, hungover, key, earring, map)
        else:
            return 'Þessi hlutur er ekki hér'

class Forrest(Room):
    def __init__(self):
        self.name = 'Skógur'
        self.things = ['villimaður']
        self.villimadur = Thing.Villimadur()
        self.description = """
Þú ert í skóginum. Það er þétt milli trjáa og þú sérð ekki mikið. Skyndilega
kemur <villimaður> hlaupandi úr skóginum, hann er kviknakinn fyrir utan
litla lendarskýlu. Hann stoppar hjá þér.
        """
        self.hidden = False
        super(Forrest, self).__init__(self.name, self.hidden)

    def whatshere(self):
        return self.things

    def whereami(self):
        return self.description

    def wherecanigo(self, map):
        return '<káeta> <bar> <strönd>'

def interact(self, thing, hungover, key, earring, map):
    if thing == 'villimaður':
        return self.villimadur.interact(thing, hungover, key, earring, map)
    else:
        return 'Þessi hlutur er ekki hér'
