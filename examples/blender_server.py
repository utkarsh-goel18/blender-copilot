import socket
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.core.parser import CommandParser
from src.core.executor import CommandExecutor

HOST = "127.0.0.1"
PORT = 5000

parser = CommandParser()
executor = CommandExecutor()

executor.controller.clear_scene()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Listening on {HOST}:{PORT}")

conn, addr =  server.accept()

print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)

    if not data:
        break

    command = data.decode()
    print("Received command: ", command)

    try:
        print("1. Parsing ...")
        parsed = parser.parse(command)

        print(parsed)

        print("2. Executing ...")
        executor.execute(parsed)

        print("3. Finished")

        conn.send(b"OK")

    except Exception as e:
        print("ERROR: ", e)
        conn.send(str(e).encode())

conn.close()
server.close()