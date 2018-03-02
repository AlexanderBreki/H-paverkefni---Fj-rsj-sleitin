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

    # Endalaus While lykkja til að hafa samskipti við server clasa
    while True:
        # Tökum við skilaboðum
        recive_msg = clientrecive.recv(2048).decode('utf -8')
        print (recive_msg)

        # Sendum skilaboð
        send_msg = input("-> ")

        if (send_msg == 'exit'):
            break

        if (send_msg == 'help'):
            print (helpme)
            send_msg = input("-> ")

        clientsend.send(send_msg.encode())

    # Lokum socket-unum
    clientrecive.close()
    clientsend.close()

if __name__ == '__main__':
    main()
