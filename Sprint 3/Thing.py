class Thing():
    def __init__(self, name):
        self.name = name # String
    def getName(self):
        return self.name

class Locker(Thing):
    def __init__(self):
        self.name = 'Skápur'
        self.msglocked = 'Skápurinn er læstur. Það er skráargat á hurðinni en það er enginn lykill í skránni.'
        self.msgopen = 'Fjársjóðurinn er fundinn! Til hamingju þú vannst'
        super(Locker, self).__init__(self.name)
    def interact(self, thing, hungover, key, earring, map):
        if key:
            return '0' + self.msgopen
        else:
            return '0' + self.msglocked

class Desk(Thing):
    def __init__(self):
        self.name = 'Skrifborð'
        self.msg = 'Á borðinu eru stórir staflar af bókum og rifið landakort. Í borðskúffunni er hálfétið epli sem er farið að mygla.'
        super(Desk, self).__init__(self.name)
    def interact(self, thing, hungover, key, earring, map):
        return '0' + self.msg

class Bed(Thing):
    def __init__(self):
        self.name = 'Rúm'
        self.msg = 'Rúmið er allt í óreiðu en þar er ekkert að finna nema hálftóma <viskíflösku>. Um borð í skipinu er nóg af rommi en viskíflöskur fást bara á barnum. Þú stingur flöskunni í jakkavasann.'
        super(Bed, self).__init__(self.name)
    def interact(self, thing, hungover, key, earring, map):
        return '0' + self.msg

class Bartender(Thing):
    def __init__(self):
        self.name = 'Barþjónn'
        self.msg = 'Þú sýnir barþjóninum viskíflöskuna. Hann yppir öxlum og hristir hausinn, þeir selja ekki þessa tegund á barnum.'
        super(Bartender, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return '0' + self.msg

class Nonni(Thing):
    def __init__(self):
        self.name = 'Nonni'
        self.msg = 'Fyrir framan Nonna er fjöldi tómra glasa, hann umlar örlítið þegar þú ávarpar hann, þegar þú stjakar við honum snýr hann sér við og þú sérð að hann er mjög fullur. Hann segist geta hjálpað þér ef þú svarar einni spurningu.'
        self.question = 'Hver er munurinn á viskí og koníaki?'

    def interact(self, thing, hungover, key, earring, map):
        return '0' + self.msg

class Josefina(Thing):
    def __init__(self):
        self.name = 'Jósefína'
        self.emptyhandedmsg = 'Jósefína slær þig utan undir fyrir ódæðissemi gærkvöldsins. Hún spyr þig hvernig þú vogir þér að koma til hennar tómhentur.'
        self.msg = 'Hún þakkar þér fyrir gærkvöldið og réttir þér nokkur ópíumlauf til að rétta þig af. Hún minnist á að þú hafir talað mikið um Einar gamla og ráðleggur þér að tala við hann'

    def interact(self, thing, hungover, key, earring, map):
        if earring:
            return '0' + self.msg
        else:
            return '2' + self.emptyhandedmsg

class Einar(Thing):
    def __init__(self):
        self.name = 'Einar'
        self.hungovermsg = 'Gamli maðurinn er gallharður bindindismaður, hann finnur áfengislyktina af þér og slær þig með þungum göngustaf.'
        self.msg = 'Einar muldrar eitthvað og lætur þig fá dularfullt kort sem leiðir þig að skóginum'
        self.hungover = True

    def interact(self, thing, hungover, key, earring, map):
        if self.hungover:
            # 2 Tekur eitt líf af leikmanni
            return '2' + self.hungovermsg
        else:
            # 3 breytir boolean gildinu hjá player í True
            return '3' + self.msg

class Kristjan(Thing):
    def __init__(self):
        self.name = 'Kristján'
        self.msg = 'setja skilaboð hér'

    def interact(self, thing, hungover, key, earring, map):
        return self.msg

class Kona(Thing):
    def __init__(self):
        self.name = 'Kona'
        self.msg = 'setja skilaboð hér'

    def interact(self, thing, hungover, key, earring, map):
        return self.

class Skur(Thing):
    def __init__(self):
        self.name = 'Kona'
        self.msg = 'setja skilaboð hér'

    def interact(self, thing, hungover, key, earring, map):
        return self.msg

class Villimadur(Thing):
    def __init__(self):
        self.name = 'villimaður'
        self.msg = 'setja skilaboð hér'

    def interact(self, thing, hungover, key, earring, map):
        return self.msg
