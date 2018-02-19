import socket
import random
import sys

def Main():
    # Búum til socket.
    host = "127.0.0.1"
    port = 5000
    mySocket = socket.socket()
    mySocket.bind((host,port))

    # Leitum að client sem vill tengjast socket-inu
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

# ***************************************************************************************************
# Föll fyrir virkni leiksins, búið er að breyta þeim til að virka á server/client formi.

# ***************************************************************************************************

# Endalaus while lykkja sem notuð er til að hafa samskipti við client hluta. Hún er brotin ef client
# hluti sendir ekki lengur gögn.
    while True:
        # Spyrjum client hluta hvor hann vilji spila roulette leikinn.
        msg = "Welcome do you want to play roulette? \n<Enter 'yes' to play>"
        conn.send(msg.encode())

        # Tökum á móti gögnum/skilaboðum frá client hluta.
        datain = conn.recv(1024).decode()

        # Ef client hluti sendi ekki neitt þá brjótum við lykkjuna.
        if not datain:
                break

        # Ef client hluti vill spila leikninn þá köllum við á fallið fyrir leikinn.
        if str(datain) == "yes":
            roulette_sim(money, losses)
    conn.close()

# Köllum á main fallið.
Main()
