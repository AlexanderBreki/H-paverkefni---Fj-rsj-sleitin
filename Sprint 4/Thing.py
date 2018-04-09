class Thing():
    def __init__(self, name):
        self.name = name # String
    def getName(self):
        return self.name

class Locker(Thing):
    def __init__(self):
        self.name = 'Skápur'
        self.msglocked = """
Skápurinn er læstur. Það er skráargat á hurðinni en það er enginn lykill í
skránni.
"""
        self.msgopen =  """
Fjársjóðurinn er fundinn! Til hamingju þú vannst.
"""
        super(Locker, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        if key:
            return '0' + self.msgopen
        else:
            return '8' + self.msglocked

class Desk(Thing):
    def __init__(self):
        self.name = 'Skrifborð'
        self.msg = """
Á borðinu eru stórir staflar af bókum og rifið landakort. Í borðskúffunni
er hálfétið epli sem er farið að mygla.
"""
        super(Desk, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return '0' + self.msg

class Bed(Thing):
    def __init__(self):
        self.name = 'Rúm'
        self.msg = """
Rúmið er allt í óreiðu en þar er ekkert að finna nema hálftóma viskíflösku.
Um borð í skipinu er nóg af rommi en viskíflöskur fást bara á barnum. Þú
stingur flöskunni í jakkavasann.
"""
        super(Bed, self).__init__(self.name)
    def interact(self, thing, hungover, key, earring, map):
        return '0' + self.msg

class Bartender(Thing):
    def __init__(self):
        self.name = 'Barþjónn'
        self.msg1 = """
Þú sýnir barþjóninum viskíflöskuna. Hann yppir öxlum og hristir hausinn,
þeir selja ekki þessa tegund á barnum.
"""
        self.msg2 = """
Barþjónninn nennir ekki að tala við þig.
"""
        self.used = False
        super(Bartender, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        if self.used == True:
            self.used = True
            return '0' + self.msg2
        else:
            return '0' + self.msg1

class Nonni(Thing):
    def __init__(self):
        self.name = 'Nonni'
        self.msg = """
Fyrir framan Nonna er fjöldi tómra glasa, hann umlar örlítið þegar þú
ávarpar hann, þegar þú stjakar við honum snýr hann sér við og þú sérð að
hann er mjög fullur. Hann segist geta hjálpað þér ef þú svarar einni
spurningu.

Hver er munurinn á viskí og koníaki?
<A>: Viskí er ekki eimað
<B>: Koníak er eimað úr víni en viskí úr korni.
<C>: Viskí þarf að koma frá Frakklandi til að kallast koníak.
<D>: Viskí er geymt lengi í tunnum en ekki koníak.
"""
        super(Nonni, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return '7' + self.msg

    def question(self, thing):
        if thing == 'A':
            return '0' + 'Veistu ekki neitt litli kútur? Reyndu aftur'
        elif thing == 'B':
            return '0' + """
Nonni segir þér að þið voruð að synda í sjónum á ströndinni í gærkvöldi og
rákust á róna sem býr á ströndinni, hann veit kannski eitthvað um hvar
fjársjóðurinn er.
"""
        elif thing == 'C':
            return '0' + 'Veistu ekki neitt litli kútur? Reyndu aftur'
        elif thing == 'D':
            return '0' + 'Veistu ekki neitt litli kútur? Reyndu aftur'
        else:
            return '0' + 'Þetta er ekki möguleiki, reyndu aftur'

class Josefina(Thing):
    def __init__(self):
        self.name = 'Jósefína'
        self.emptyhandedmsg = """
Jósefína slær þig utan undir fyrir ódæðissemi gærkvöldsins. Hún spyr þig
hvernig þú vogir þér að koma til hennar tómhentur.
"""
        self.msg = """
Hún þakkar þér fyrir gærkvöldið og réttir þér nokkur ópíumlauf til að
rétta þig af. Hún minnist á að þú hafir talað mikið um Einar gamla og
ráðleggur þér að tala við hann.
"""
        super(Josefina, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        if earring:
            return '4' + self.msg
        else:
            return '2' + self.emptyhandedmsg

class Einar(Thing):
    def __init__(self):
        self.name = 'Einar'
        self.hungovermsg = """
Gamli maðurinn er gallharður bindindismaður, hann finnur áfengislyktina af
þér og slær þig með þungum göngustaf.
"""
        self.msg = """
Einar muldrar eitthvað og lætur þig fá dularfullt kort sem leiðir þig að
skóginum.
"""
        super(Einar, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        if hungover == True:
            # 2 Tekur eitt líf af leikmanni
            return '2' + self.hungovermsg
        else:
            # 3 breytir boolean gildinu hjá player í True
            return '3' + self.msg

class Kristjan(Thing):
    def __init__(self):
        self.name = 'Kristján'
        self.msg = '7' + """
Róninn gælir við kött og segist vera svangur. Hann neitar að svara
spurningum þínum nema hann fái að borða.

Hvernig mat gefurðu Kristjáni?
<A>: Grænmeti.
<B>: Vegaborgara.
<C>: Kjúkling.
<D>: Samloku.
"""
        super(Kristjan, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return self.msg

    def question(self, thing):
        if thing == 'A':
            return '5' + """
Rétt svar, róninn er sáttur og segir þér hvað gerðist kvöldið áður, þið
Nonni voruð ekki einir á ströndinni þið voruð með tveimur konum og fóruð
með þeim á barinn. Róninn segir þér að færa henni eitthvað fallegt fyrir
það sem þú gerðir í gær. Hann tekur fallega skel sem hann fann á
ströndinni úr hliðartösku sinni og gefur þér hana.
"""
        elif thing == 'B':
            return '5' + """
Rétt svar, Vegaborgarinn er ekki vegan en Kristján Róni veit það ekki. Þú
platar ofan í hann kjöt.

Hann er sáttur og segir þér hvað gerðist kvöldið áður, þið
Nonni voruð ekki einir á ströndinni þið voruð með tveimur konum og fóruð
með þeim á barinn. Róninn segir þér að færa henni eitthvað fallegt fyrir
það sem þú gerðir í gær. Hann tekur fallega skel sem hann fann á
ströndinni úr hliðartösku sinni og gefur þér hana.
"""
        elif thing == 'C':
            return '2' + """
Rangt svar, róninn er vegan. Hann verður reiður og kastar einum ketti í þig.
Kötturinn bregst ókvæða við og klórar þig.
"""
        elif thing == 'D':
            return '2' + """
Rangt svar, það var ostur á samlokunni og róninn er vegan. Hann bítur þig.
"""
        else:
            return '0' + 'Þetta er ekki möguleiki, reyndu aftur'

class Kona(Thing):
    def __init__(self):
        self.name = 'Kona'
        self.msg = """
Þú gengur upp að konunni og sérð að þetta er Pamela Anderson, hún er með
stjörnustæla og hrindir þér á hrúgu af kröbbum
"""
        super(Kona, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return '2' + self.msg

class Skur(Thing):
    def __init__(self):
        self.name = 'skúr'
        self.msg = """
Skúrinn er hrörlegur og gamall, innan í honum er mikið af gömlu drasli.
Ofan á hrúgunni finnur þú flösku af framandi drykk, Gatorade. Þú drekkur
innihald flöskunnar og losnar við þynnkuna
"""
        super(Skur, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return '4' + self.msg

class Villimadur(Thing):
    def __init__(self):
        self.name = 'Villimaður'
        self.msg = '7' + """
Villimaðurinn talar góða íslensku. Þú tekur eftir því að hann heldur á
gamalli útgáfu af Hobbitanum eftir J.R.R. Tolkien. Hann neitar að svara
spurningum nema þú sigrir hann í gátukeppni.

Fyrsta spurning:
Hvernig kista er án lama, loks eða lykils, leynir þó gullnum sjóði?
<A>: Mannsálin.
<B>: Vinátta.
<C>: Egg.
"""
        super(Villimadur, self).__init__(self.name)

    def interact(self, thing, hungover, key, earring, map):
        return self.msg

    def question(self, thing):
        if thing == 'A':
            return '2' + """
Rangt svar. Villimaðurinn slær þig.
"""
        elif thing == 'B':
            return '2' + """
Rangt svar. Villimaðurinn slær þig.
"""
        elif thing == 'C':
            return '6' + """
Rétt svar! Þú ert helvíti seig(ur)

Villimaðurinn teygir sig ofan í sveitta lendarskýluna og réttir þér lykil.
Hann segir að þú hafir misst lykilinn á ströndinni.
"""
        else:
            return '0' + 'Þetta er ekki möguleiki, reyndu aftur'
