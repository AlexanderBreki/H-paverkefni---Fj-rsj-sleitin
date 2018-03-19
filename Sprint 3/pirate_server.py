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
        self.story = ('1' +
"""Þú ert sjóræningi sem fékkst þér einum of mikið af rommi í gærkvöldi. Þér var treyst fyrir því að passa upp á fjársjóðskistu en eftir læti gærkvöldsins hefur þú ekki hugmynd um hvar hún er niður komin. Þú vaknar í káetunni þinni og þarft að leita að fjársjóðnum.
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

        recive_msg = self.crecive.recv(2048).decode('utf -8')
        while recive_msg != 'exit':
            print ('From client: ' + recive_msg)

            # Leikmaður kallar á hlut
            if recive_msg in self.player.location.things:
                interact_msg = self.player.location.interact(recive_msg, self.player.hungover, self.player.key, self.player.earring, self.player.map)
                send_msg = interact_msg[1:]
                if interact_msg == '0':
                    send_msg = interact_msg[1:]
                if interact_msg[0] == '1':
                    self.player.getLife()
                    send_msg = interact_msg[1:] + '\nÞú færð eitt líf!'
                elif interact_msg[0] == '2':
                    self.player.loseLife()
                    send_msg = interact_msg[1:] + '\nÞú missir eitt líf!'
                self.csend.send(bytes(('1' + send_msg),'utf -8'))

            # Leikmaður kallar á whatshere
            elif recive_msg == 'whatshere':
                send_msg = self.player.location.whatshere()
                self.csend.send(bytes(('1' + send_msg),'utf -8'))

            # Leikmaður kallar á whereami
            elif recive_msg == 'whereami':
                send_msg = self.player.location.whereami()
                self.csend.send(bytes(('1' + send_msg),'utf -8'))

            # Leikmaður kallar á changeroom
            elif recive_msg == 'changeroom':
                send_msg = 'Í hvaða herbergi vilt þú fara? ' + self.player.location.wherecanigo()
                self.csend.send(bytes(('1' + send_msg),'utf -8'))
                recive_msg = self.crecive.recv(2048).decode('utf -8')
                send_msg = self.player.changeroom(recive_msg)
                self.csend.send(bytes(('1' + send_msg),'utf -8'))

            # Ef skipunin passar ekki við neina löglega skipun
            else:
                send_msg = 'Ekki lögleg skipun'
                self.csend.send(bytes(('1' + send_msg),'utf -8'))

            recive_msg = self.crecive.recv(2048).decode('utf -8')







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
        print(crecive)
        # Búum til PirateGame object
        PirateGame_ob = PirateGame(csend, crecive)

        # Byrjun leikinn
        PirateGame_ob.PlayGame()
        break


if __name__ == '__main__':
    main()
