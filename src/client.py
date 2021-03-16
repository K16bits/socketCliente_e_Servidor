import socket
HOST = ''     
PORT = 3000       
tcp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest = (HOST, PORT)

print ('Client iniciado...')
msgClient = ("msg do cliente").encode('UTF-8')
tcp.sendto(msgClient,dest)

msgServer,addrServer = tcp.recvfrom(1024)
print(msgServer)

tcp.close()