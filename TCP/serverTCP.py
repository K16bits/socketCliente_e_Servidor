import socket
HOST = 'localhost'
PORT = 3000

tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
orig = (HOST,PORT)
tcp.bind(orig)
tcp.listen(1)

print("Server TCP está rodando...")
while True:
    con,client = tcp.accept()
    print("Cliente conectado: ",client)
    while True:
        msg = con.recv(1024)
        if not msg:break
        print("Client message: ",client,msg.decode("UTF-8"))
    print("Finalizando a conexão com o cliente:",client)
    con.close()
#udp.close()
