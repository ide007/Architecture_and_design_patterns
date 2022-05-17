import socket


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = ('127.0.0.1', 8001)
server_sock.bind(server_adress)
server_sock.listen(1)

while True:
    print('Server ready to connect')
    client_connection, client_address = server_sock.accept()
    print(f'Connection with : {client_address}.')
    data = client_connection.recv(1024).decode()
    print(data)
    client_connection.close()
