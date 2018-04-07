import socket
import select
import time


# ******************************************************************************
# Hér kemur client clasi
# ******************************************************************************

# Main forrit
def main():
    # Búum til tvö socket, eitt til að senda skilaboð og annað til að taka á móti
    clientrecive = socket.socket(socket.AF_INET , socket. SOCK_STREAM )
    clientsend = socket.socket(socket.AF_INET , socket. SOCK_STREAM )

    # clientrecive tengist serversend og clientsend tengist serverrecive
    clientrecive.connect (('localhost',3002))
    clientsend.connect (('localhost',3003))

    helpme = "Hér koma upplýsingar um hvernig leikurinn virkar"

    send_msg = ''
    recive_msg = ''

    Game_Over = False
    # Endalaus While lykkja til að hafa samskipti við server clasa
    while send_msg != 'exit' and Game_Over == False:
        # Tökum við skilaboðum
        recive_msg = clientrecive.recv(2048).decode('utf -8')
        # Prentum skilaboðin
        print (recive_msg[1:])

        # Athugum hvort server vilji svar eða ekki
        if recive_msg[0] == '1':
            # Tökum við skipun frá lyklaborði
            send_msg = input("-> ")
            # Sendum skilaboð á server
            clientsend.send(send_msg.encode())
        if recive_msg[0] == '3':
            Game_Over = True

    # Lokum socket-unum
    clientrecive.close()
    clientsend.close()

if __name__ == '__main__':
    main()
