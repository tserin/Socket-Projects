import socket
HEADERSIZE = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    HOST = socket.gethostname()
    PORT = 9999
    c.connect((HOST,PORT))
    while True:
        full_msg = ''
        new_msg = True
        while True:
            msg = c.recv(16)
            if new_msg:
                print(f"New mesage length : {msg[:HEADERSIZE]}")
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg.decode("utf-8")

            if len(full_msg) - HEADERSIZE ==msglen:
                print("full msg recvd")
            # if not msg:
            #     print("Empty")
            #     break
                print(msg.decode("utf-8"))
                print(full_msg[HEADERSIZE:])
                new_msg = True
                full_msg =''
    print(full_msg)

#netstat -an
#lsof -i -n
