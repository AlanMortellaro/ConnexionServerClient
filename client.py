import socket
import os

ok = ''
def cmdrecv():
    cmd = server_co.recv(1024)
    cmd = cmd.decode()
    return cmd

def sendconfirm():
    if valueCmd == 'ping':
        server_co.send("pong")
    else:
        server_co.send(b'Command recieved successfully')

hote = 'localhost'
port = 25565
server_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_co.connect((hote, port))
print("[*] Connected")
msg = b''
while msg != b'stop':
    valueCmd = cmdrecv()
    sendconfirm()
    print(valueCmd)
print("[*] Session Close")
server_co.close()
