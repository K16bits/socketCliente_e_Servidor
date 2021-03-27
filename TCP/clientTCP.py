import socket
HOST = ''     
PORT = 3000       
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)
print ('Client iniciado...')


msgClient = input('mande uma mensagem para o server TCP: ')
while msgClient != 'x':
    tcp.send(bytes(msgClient,"UTF-8"))
    msgClient = input('mande uma mensagem para o server TCP: ')
tcp.close()

