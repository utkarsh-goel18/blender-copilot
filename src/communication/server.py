import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server listening on {HOST}:{PORT}")

conn, addr = server.accept()

print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)

    if not data:
        break

    print("Received: ", data.decode())

conn.close()
server.close()