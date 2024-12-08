import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.bind(('127.0.0.1', 55555))

s.listen()

while True:
    client ,address = s.accept()
    print(f"Got connection from {address}")
    client.send(b"Hello , client! you are connected")
    client.close()
    
