import socket
import time
HEADERSIZE = 10
#Create socket
#By default, IPV4 and TCP connection socket will be created

s = socket.socket()
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.Sock_DGRAM for udp
HOST = socket.gethostname()
PORT = 9999
#Bind host and port

s.bind((HOST, PORT))
# s.bind((socket.gethostname(), 9999))
#(host, port, flowinfo, scopeid) for IPv6.
#Listen to the connection
s.listen(4) #accepts only three connection a t time


while True:
    conn, addr = s.accept()
    print(f"Connection to {addr} established")
    # Receive data from the client and verify the request
    # data = conn.recv(1024)
    # if not data:
    #     print("Empty Request")
    #     break
    msg = "Welcome to the Server"
    msg = f'{len(msg):<{HEADERSIZE}}' +msg
    print(msg)
    conn.send(bytes(msg,"utf-8"))
    # conn.close()
    #conn.sendall("to send all data use sendall")


    while True:
        time.sleep(3)
        msg =f"The time is {time.time()}"
        msg = f'{len(msg):< {HEADERSIZE}}' +msg
        conn.send(bytes(msg, "utf-8"))





