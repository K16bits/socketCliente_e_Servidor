import socket
HOST = '' #localhost
PORT = 3000

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest = (HOST,PORT)

print('Client UDP on\npara finalizar a conexão digite x')
msg = input("Envie sua mensagem para o servidor: ")
while msg != 'x':
    udp.sendto(bytes(msg, 'utf-8'),dest)
    msg = input()

udp.close()



#tcp.send(bytes(msg, 'utf-8'))