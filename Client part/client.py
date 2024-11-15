# this script will run on the fathers laptop to get data from Raspberry Pi

import socket

s = socket.socket()
s.connect(("192.168.0.100", 12345))
s.send(b"give me the data")

path = "client_files"

with open(f"{path}\\test.out", "wb") as f_out:
    last_2_got = ["", ""]
    ind = 0
    while True:
        data = s.recv(2 ** 20)

        last_2_got[ind] = data.decode()
        ind = (ind + 1) % 2

        f_out.write(data)

        if "end of all files" in last_2_got[(ind + 1) % 2] + last_2_got[ind]:
            break
s.close()
