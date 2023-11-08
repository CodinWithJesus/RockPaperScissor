import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(1)

print('TCP Server is listening...')

while True:
    conn, addr = server_socket.accept()
    print(f'Connection address: {addr}')

    data = conn.recv(1024).decode('utf-8')

    if data == "Rock":
        result = "You win!"
    elif data == "Paper":
        result = "You lose!"
    elif data == "Scissors":
        result = "It's a draw!"
    else:
        result = "Invalid choice!"

    conn.send(result.encode('utf-8'))
    conn.close()