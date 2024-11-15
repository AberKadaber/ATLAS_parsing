# this script will be run on the Raspberry Pi

import socket
import os

# here will be new path
path = "D:\FathersWork\AtlasSystem\server_files"


s = socket.socket()
s.bind(("", 12345))

s.listen(1)
conn, addr = s.accept()
while True:
    got = conn.recv(1024)
    if got == b"give me the data":
        for filename in os.listdir(path):
            with open(f"{path}\\{filename}", "rb") as f:
                conn.send(f"filename: {filename}\n".encode())
                conn.send(f.read())
        conn.send(b"end of all files")
        conn.close()
        s.close()
        s = socket.socket()
        s.bind(("", 12345))
        s.listen(1)
        conn, addr = s.accept()
        print("restart server")
