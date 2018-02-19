import socket
import select
import sys
import time
import random

class roulette_s(object):

#Constructor: instantiate a new object
    def __init__(self, money, losses):
        self.money= money
        self.losses= losses

#Destrocture: executed when object is "removed"
    def __del__(self):
        print('at del: {0} and {1}'.format(self.money, self.losses))

#How much do you want to bet?
    def roulette_sim(self,c):
        while(1):
            try:
                msg='How much do you want to bet? ''\n'
                c.send(bytes(msg ,'utf -8'))
                buf = c.recv(1024)
                msg = buf.decode('utf -8')
                bet=int(msg)
                print(msg ,end='')
                break
            except ValueError:
                print ('You need to input a number')
        if bet > self.money:
            self.bet_too_much(c)
        else:
            self.red_or_black(bet, c)

# Prevents one from betting more money than one has
    def bet_too_much(self,c):
        msg='You do not have all that money. Please bet again ''\n'
        c.send(bytes(msg ,'utf -8'))
        self.roulette_sim(c)

# Asks user to select red or black, starts the sim, modifies money/losses
    def red_or_black(self, bet, c):
        msg='OK, you bet '+str(bet)+'  Red or Black?''\n'
        c.send(bytes(msg ,'utf -8'))
        buf = c.recv(1024)
        answer = buf.decode('utf -8')
        number = random.randint(1, 2)
        if number == 1 and answer == "Red":
            self.money += 10*bet
            msg = 'You win! You now have money: '+ str(self.money)+'   Your losses are: '+str(self.losses)+'\n'
        elif number == 2 and answer == "Black":
            self.money += 10*bet
            msg = 'You win! You now have money: '+ str(self.money)+'   Your losses are: '+str(self.losses)+'\n'
        else:
            print ("You lost!")
            self.money -= bet
            self.losses += bet
            msg = 'You lost! You now have money: '+ str(self.money)+'  Your losses are: '+str(self.losses)+'\n'
        c.send(bytes(msg ,'utf -8'))
        self.replay(c)

# Asks user whether he/she wants to play again
    def replay(self,c):
        msg = 'Do you want to play again?'+'\n'
        c.send(bytes(msg ,'utf -8'))
        buf = c.recv(1024)
        msg = buf.decode('utf -8')
        print(msg ,end='')
        if msg == "y" and self.money > 0:
            self.roulette_sim(c)
        elif self.money == 0:
            msg = 'OK, your acount is empty'+'\n'
        else:
            msg = 'Collect your money'+'\n'
        c.send(bytes(msg ,'utf -8'))
        
#Main program
def main():
    s = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
    port = 3002
    cnt=0

    try:
        s.bind (('',port))
    except socket.error as msg:
        print( 'Bind failed - aborting' )
        sys.exit ()
    s.listen (5)
    roul= roulette_s(5000, 0)
    while True:
        c,addr = s.accept()
        print('New connection:', addr)
        c.send(b'Hello\n')
        cnt += 1
        time.sleep (1)
        msg='Your id is '+str(cnt)+'\n'
        c.send(bytes(msg ,'utf -8'))
        roul.roulette_sim(c)

if __name__ == '__main__':
    main()
