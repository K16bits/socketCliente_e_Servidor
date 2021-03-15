import socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 3000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print ('Cliente se conector com o servidor\n')
msg = input("envie sua msg ao servidor: ").encode('utf-8')
tcp.send (msg)
msg = input("envie sua msg ao servidor: ")

tcp.close()