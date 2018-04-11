import socket
import select
import time

# Main forrit
def main():
    # Búum til tvö socket, eitt til að senda skilaboð og annað til að taka á móti
    clientrecive = socket.socket(socket.AF_INET , socket. SOCK_STREAM )
    clientsend = socket.socket(socket.AF_INET , socket. SOCK_STREAM )

    # clientrecive tengist serversend og clientsend tengist serverrecive
    clientrecive.connect (('localhost',3002))
    clientsend.connect (('localhost',3003))

    send_msg = ''
    recive_msg = ''

    Game_Over = False
    # Endalaus While lykkja til að hafa samskipti við server clasa.
    while Game_Over == False:
        # Tökum við skilaboðum.
        recive_msg = clientrecive.recv(2048).decode('utf -8')
        # Prentum skilaboðin.
        print (recive_msg[1:])

        # Kóði 1 þýðir að server vill fá svar frá client.
        if recive_msg[0] == '1':
            # Tökum við skipun frá lyklaborði.
            send_msg = input("-> ")
            # Sendum skilaboð á server.
            clientsend.send(send_msg.encode())

        # Kóði 3 þýðir að loka leiknum.
        if recive_msg[0] == '3':
            Game_Over = True

    # Lokum socket-unum
    clientrecive.close()
    clientsend.close()

if __name__ == '__main__':
    main()
