import socket
HOST = 'localhost'
PORT = 3000

tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
orig = (HOST,PORT)
tcp.bind(orig)
tcp.listen()

while True:
    conn, client = tcp.accept()
    print("Conectado por: ", client)
    msg = conn.recv(1024)
    print("Client msg:", msg)
    conn.close()