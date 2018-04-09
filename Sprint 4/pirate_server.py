import socket
import select
import sys
import time
import random
import Player

# ******************************************************************************
# Hér kemur server clasi
class PirateGame(object):
    # Skilgreinum hér grunn attribute fyrir leikinn

    # Smiður: Búum til nýjan leik.
    def __init__(self, csend, crecive):
        self.csend = csend
        self.crecive = crecive
        self.player = Player.Player()
        self.help = '1' + """Hér koma help skilaboð."""
        self.story = ('1' +
"""
Þú ert sjóræningi sem fékkst þér einum of mikið af rommi í gærkvöldi. Þér
var treyst fyrir því að passa upp á fjársjóðskistu en eftir læti
gærkvöldsins hefur þú ekki hugmynd um hvar hún er niður komin. Þú vaknar í
káetunni þinni og þarft að leita að fjársjóðnum.

Leikurinn er einfaldur. Þú byrjar í einu herbergi, þú getur séð hvaða
herbergi það er með skipuninni <whereami>, þar inni eru hlutir sem þú getur
valið að skoða nánar. Skipunin <whatshere> gefur þér lýsingu á herberginu,
allir hlutir sem þú getur skoðað eru inni í <>. Skrifaðu nafnið á þeim til
að skoða þá nánar. Þegar þú vilt færa þig milli herbergja getur þú fengið
lista yfir alla mögulega áfangastaði með skipuninni <wherecanigo>, og farið
svo í annað herbergi með skipuninni <changeroom>.
""")
        self.skull = ('0' +
"""

                                 $$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$
                            $$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$"   "$$$"   "$$$$$$
                         "$$$$"      u$u       $$$$"
                          $$$u       u$u       u$$$
                          $$$u      u$$$u      u$$$
                           "$$$$uu$$$   $$$uu$$$$"
                            "$$$$$$$"   "$$$$$$$"
                              u$$$$$$$u$$$$$$$u
                               u$"$"$"$"$"$"$u
                    uuu        $$u$ $ $ $ $u$$       uuu
                   u$$$$        $$$$$u$u$u$$$       u$$$$
                    $$$$$uu      "$$$$$$$$$"     uu$$$$$$
                  u$$$$$$$$$$$uu    '''''   uuuu$$$$$$$$$$
                  $$$$'''$$$$$$$$$$uuu   uu$$$$$$$$$'''$$$"
                              ""$$$$$$$$$$$uu ''$''
                         uuuu ""$$$$$$$$$$uuu
                 u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
                 $$$$$$$$$$''''           ""$$$$$$$$$$$"
                  "$$$$$"                      ""$$$$""
                    $$$"                         $$$$
***************************************************************************
*************************** TÝNDI FJÁRSJÓÐURINN ***************************
***************************************************************************
""")


    # Eyðir: Eyðir socket-unum þegar við hættum að nota hlutinn
    def __del__(self): pass
        #print('at del: {0} and {1}'.format(self.csend, self.crecive))

    # Fall sem sendir hauskúpu og titil leiksins
    def displayskull(self):
        self.csend.send(bytes((self.skull),'utf -8'))

    # Fall sem sendir upphafsögu leiksins
    def displaystory(self):
        self.csend.send(bytes((self.story),'utf -8'))

    def PlayGame(self):
        # Sendum upphafskilaboð og baksögu aðalkarakters á client
        self.displayskull()
        self.displaystory()

        # Tökum við upphafskilaboðum frá client klasa
        #recive_msg = self.crecive.recv(2048).decode('utf -8')
        Game_Over = False

        # Á meðan client klasinn sendir ekki 'exit' þá höldum við áfram
        while Game_Over == False:
            recive_msg = self.crecive.recv(2048).decode('utf -8')
            print ('From client: ' + recive_msg)

            # Leikmaður vill hætta.
            if recive_msg == 'exit':
                Game_Over = True

            # Leikmaður kallar á hjálp.
            if recive_msg == 'help':
                send_msg = self.help

            # Leikmaður kallar á hlut sem er inni í rúverandi herbergi
            if recive_msg in self.player.location.things:

                # Köllum á interact fall herbergisins
                interact_msg = self.player.location.interact(recive_msg, self.player.hungover, self.player.key, self.player.earring, self.player.map)

                # Skilgreinum skilaboðin sem við sendum til baka, sleppum fyrsta stakinu í þeim streng
                # því hann er notaður til að skilgreina virkni hlutarins
                send_msg = interact_msg[1:]

                # Kóði 7 þýðir að við sendum á client og fáum svar til baka
                if interact_msg[0] == '7':
                    send_msg = interact_msg[1:]
                    self.csend.send(bytes(('1' + send_msg),'utf -8'))
                    recive_msg = self.crecive.recv(2048).decode('utf -8')
                    interact_msg = self.player.location.question(recive_msg)

                # Kóði 0 þýðir að ekkert gerist
                if interact_msg[0] == '0':
                    send_msg = interact_msg[1:]

                # Kóði 1 þýðir að leikmaður fær eitt líf
                if interact_msg[0] == '1':
                    self.player.getLife()
                    send_msg = interact_msg[1:] + '\nÞú færð eitt líf! Núna áttu ' + str(self.player.lifes) + ' líf eftir \n'

                # Kóði 2 þýðir að leikmaður missir eitt líf
                elif interact_msg[0] == '2':
                    self.player.loseLife()
                    send_msg = interact_msg[1:] + '\nÞú missir eitt líf! Núna áttu ' + str(self.player.lifes) + ' líf eftir \n'

                # Kóði 3 þýðir að leikmaður fær landakort
                elif interact_msg[0] == '3':
                    self.player.map = True
                    send_msg = interact_msg[1:] + '\nÞú ert kominn með landakort \n'

                # Kóðinn 4 þýðir að leikmaður er ekki lengur þunnur
                elif interact_msg[0] == '4':
                    self.player.hungover = False
                    send_msg = interact_msg[1:] + '\nÞú ert ekki lengur þunnur \n'

                # Kóði 5 þýðir að leikmaður fær skel
                elif interact_msg[0] == '5':
                    self.player.earring = True
                    send_msg = interact_msg[1:] + '\nÞú ert kominn með fallega skel \n'

                # Kóði 6 þýðir að leikmaður er með lykilinn að skápnum
                elif interact_msg[0] == '6':
                    self.player.key = True
                    send_msg = interact_msg[1:] + '\nÞú ert kominn með lykilinn \n'

                # Kóði 8 þýðir að leikmaður er með hefur unnið leikinn
                elif interact_msg[0] == '8':
                    send_msg = interact_msg[1:]
                    Game_Over = True

            # Leikmaður kallar á whatshere
            elif recive_msg == 'whatshere':
                send_msg = self.player.location.whatshere()

            # Leikmaður kallar á whereami
            elif recive_msg == 'whereami':
                send_msg = self.player.location.whereami()

            # Leikmaður kallar á wherecanigo
            elif recive_msg == 'wherecanigo':
                send_msg = self.player.location.wherecanigo(self.player.map)

            # Leikmaður kallar á changeroom
            elif recive_msg == 'changeroom':
                send_msg = 'Í hvaða herbergi vilt þú fara? ' + self.player.location.wherecanigo(self.player.map)
                self.csend.send(bytes(('1' + send_msg),'utf -8'))
                recive_msg = self.crecive.recv(2048).decode('utf -8')
                send_msg = self.player.changeroom(recive_msg)

            # Ef skipunin passar ekki við neina löglega skipun
            else:
                send_msg = '\nEkki lögleg skipun \n'

            if self.player.isDead():
                send_msg = interact_msg[1:] + '\nÞú misstir öll lífin og takk fyrir að spila.'
                Game_Over = True
                self.csend.send(bytes(('3' + send_msg),'utf -8'))
            else:
                self.csend.send(bytes(('1' + send_msg),'utf -8'))

            #recive_msg = self.crecive.recv(2048).decode('utf -8')

# ******************************************************************************

# Main forrit
def main():
    # Búum til tvö socket, eitt til að senda skilaboð og annað til að taka á móti
    serversend = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
    serverrecive = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
    portsend = 3002
    portrecive = 3003

    # Tengjum socket-in við port.
    try:
        serversend.bind (('',portsend))
        serverrecive.bind (('',portrecive))
    except socket.error as msg:
        print( 'Bind failed - aborting' )
        sys.exit ()

    print ("Server is running:")

    # Endalaus While lykkja til að hafa samskipti við client clasa
    while True:
        # Hlustum eftir spilara sem vill tengjast
        serversend.listen (5)
        serverrecive.listen (5)

        # Tökum á móti tengingu frá client clasa
        csend,addr = serversend.accept()
        crecive,addr = serverrecive.accept()

        # Prentum út address-ið sem var að tengjast servernum
        print('New connection address:', addr)

        # Búum til PirateGame object
        PirateGame_ob = PirateGame(csend, crecive)

        # Byrjun leikinn
        PirateGame_ob.PlayGame()
        break


if __name__ == '__main__':
    main()
