import socket
HOST = 'localhost'
PORT = 3000

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
orig = (HOST,PORT)
udp.bind(orig)

print("Server está rodando...");
while True:
    msg,client = udp.recvfrom(1024)
    print("Mensagem do Cliente: ",msg)
    msgServer = ("msg do servidor").encode('UTF-8')
    udp.sendto(msgServer,client)
#udp.close()