import socket
import select
import sys
import time
import random

# ******************************************************************************
# Hér kemur server clasi
class PirateGame(object):
    # Skilgreinum hér grunn attribute fyrir leikinn
    skull = ('\n ' +
             '                                $$$$$$$$$$$\n' +
             '                             $$$$$$$$$$$$$$$$$\n' +
             '                           $$$$$$$$$$$$$$$$$$$$$\n' +
             '                          $$$$$$$$$$$$$$$$$$$$$$$\n' +
             '                         $$$$$$$$$$$$$$$$$$$$$$$$$\n' +
             '                         $$$$$$"   "$$$"   "$$$$$$\n' +
             '                        "$$$$"      u$u       $$$$"\n' +
             '                         $$$u       u$u       u$$$\n' +
             '                         $$$u      u$$$u      u$$$\n' +
             '                          "$$$$uu$$$   $$$uu$$$$"\n' +
             '                           "$$$$$$$"   "$$$$$$$"\n' +
             '                             u$$$$$$$u$$$$$$$u\n' +
             '                              u$"$"$"$"$"$"$u\n' +
             '                   uuu        $$u$ $ $ $ $u$$       uuu\n' +
             '                  u$$$$        $$$$$u$u$u$$$       u$$$$\n' +
             '                   $$$$$uu      "$$$$$$$$$"     uu$$$$$$\n' +
             '                 u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$\n' +
             '                 $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"\n' +
             '                   """      ""$$$$$$$$$$$uu ""$"""\n' +
             '                        uuuu ""$$$$$$$$$$uuu\n' +
             '                u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$\n' +
             '                $$$$$$$$$$""""           ""$$$$$$$$$$$"\n' +
             '                 "$$$$$"                      ""$$$$""\n' +
             '                   $$$"                         $$$$"\n \n' +
             '********************************************************************* \n' +
             '************************ TÝNDI FJÁRSJÓÐURINN ************************ \n' +
             '********************************************************************* \n')
    story = " "

    # Smiður: Búum til nýjan leik.
    def __init__(self, csend, crecive):
        self.csend = csend
        self.crecive = crecive

    # Eyðir: Eyðir socket-unum þegar við hættum að nota hlutinn
    def __del__(self): pass
        #print('at del: {0} and {1}'.format(self.csend, self.crecive))

    def PlayGame(self):
        # Sendum upphafskilaboð og baksögu aðalkarakters á client
        self.displayskull()

    # Fall sem sendir upphafsögu leiksins.
    def displayskull(self):
        self.csend.send(bytes((self.skull),'utf -8'))

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

        # Búum til PirateGame object
        PirateGame_ob = PirateGame(csend, crecive)

        # Byrjun leikinn
        PirateGame_ob.PlayGame()

if __name__ == '__main__':
    main()
