import socket
HOST = '' #localhost
PORT = 3000

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

orig = (HOST,PORT)
udp.bind(orig)

print('Server UDP on')

while True:
    msg, cliente = udp.recvfrom(1024)
    print(cliente,msg.decode("UTF-8"))
udp.close