import socket
import time
host='localhost'
port=5000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
time.sleep(5)
s.sendto(b"Hello, CLient, how are you",(host,port))
msg="Bye!"
s.sendto(msg.encode(),(host,port))
s.close()
