import socket
import select
import time
from subprocess import call

class roulett_c(object):
#Constructor: instantiate a new object
    def __init__(self,s):
        self.msg2= 'OK, you bet'
        self.msg3= 'OK, your acount is empty'
        self.msg4= 'Collect your money'
        self.s= s
#Destrocture: executed when object is "removed"
    def __del__(self):
        print('at del: {}'.format(self.s))
#Start playing roulette:
    def start_playing(self):
        while True:
            # read , write , exception , 3 sec timeout
            ready = select.select ([self.s] ,[] ,[] ,3)
            if len(ready) < 1:
                break
            time.sleep (3)
            buf = self.s.recv(1024)
            msg = buf.decode('utf -8')
            print(msg ,end='')
            if msg[0] is self.msg4[0] or msg[9] is self.msg3[9]:
                break
            elif msg[0] is self.msg2[0] and msg[1] is self.msg2[1]:
                answer = input("Red or Black > ")
                self.s.send(bytes(answer,'utf -8'))
                buf = self.s.recv(1024)
                msg = buf.decode('utf -8')
                print(msg ,end='')
                time.sleep(1)
                buf = self.s.recv(1024)
                msg = buf.decode('utf -8')
                print(msg ,end='')
                msg = input('y/n> ')
            else:
                try:
                    msg = input ('My bet: ')
                    bet=int(msg)
                    msg= ''+str(bet)+'\n'
                except ValueError:
                    print ('You need to input a number')
            self.s.send(bytes(msg,'utf -8'))
        self.s.close()
#Main program
def main():
    call('clear')
    s = socket.socket(socket.AF_INET , socket. SOCK_STREAM )
    s.connect (('localhost',3002))

    roule_c= roulett_c(s)
    roule_c.start_playing()
    s.close()

if __name__ == '__main__':
    main()
