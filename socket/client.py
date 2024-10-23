import socket
if __name__ == '__main__':
    host = '192.168.59.144'
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    while True:
        message = input('Enter your message: ')
        sock.sendall(message.encode())

        response = sock.recv(1024).decode()
        print('Sender response:', response)

    sock.close()
