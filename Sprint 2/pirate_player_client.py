# Client klasi með tveimur socketum, eitt fyrir send og eitt fyrir recive.

import socket

def Main():
        # Tengjumst local socket-i.
        host = '127.0.0.1'
        port = 5000
        mySocket = socket.socket()
        mySocket.connect((host,port))

        # Prentum út upphafsskilaboð fyrir notenda.
        print ("\n \n")
        print ("***** Welcome, you have succesuflly connected to the server! *****\n")
        print ("*********** To disconnect from the server type 'exit' ************\n \n")

        # While lykkja sem stoppar bara ef skilaboðin frá notenda eru "exit".
        dataout = ""
        while dataout != 'exit':
                # Tökum við gögnum/skilaboðum frá sever hluta og prentum þau.
                datain = mySocket.recv(1024).decode()
                print (datain)
                # Fáum input frá lyklaborði og sendum á server hluta.
                dataout = input("-> ")
                mySocket.send(dataout.encode())
        mySocket.close()

# Köllum á main fall.
Main()
