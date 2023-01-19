import socket
import time

target = "127.0.0.1"
port = 9091

cmd = ""



while True:
    cmd = input("CMD&args: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((target, port))
        s.sendall(cmd.encode("utf-8"))
        data = s.recv(1024)
        print('received:   ', str(repr(data))[2:-1])
    

