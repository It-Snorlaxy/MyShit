import socket

#server information
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.107.163.11"
ADDR = (SERVER, PORT)

#Conneting to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#this encodes msg to a format that the server can decode
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
#don't mind this #print(client.recv(2048).decode(FORMAT))

#this is our way to send the msg
while True == True:
    M = input('')
    send(M)
    if M == "exit": #this gives the client a way to terminate the consol and quit in a lesss violent way
        send(DISCONNECT_MESSAGE)
        connected = False
        exit()
