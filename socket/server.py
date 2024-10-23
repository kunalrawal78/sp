import socket
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    totalclient = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(totalclient)
    connections = []
    print('Waiting for clients to connect...')
    for i in range(totalclient):
        conn, addr = sock.accept()
        connections.append((conn, addr))
        print('Connected with client', i+1, 'at', addr)
    for conn, addr in connections:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print('Received message from Sender', addr, ':', data)
            response = input('Enter your response: ')
            conn.send(response.encode())
        conn.close()
    sock.close()
