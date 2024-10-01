import socket
#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
host = '127.0.0.1'
port = 9001
try:
    s.connect((host, port))
    # we are now connected to server
    print('Client: Connected to server...')

    #--------------------------------------------------
    # single connection operation
    # data = s.recv(1024).decode() # 1024 bytes
    # print(data)
    # s.close()
    # print('Connection has been closed...')
    #--------------------------------------------------

    # Receiving information
    # while True:
    #     msg = s.recv(1024).decode()
    #     if not msg:
    #         break
    #     print(msg)
    #     data = input('Enter your response ')
    #     s.sendall(str.encode(data))

    # s.close()
    # print('Client: Connection closed...')

    # Assignment - Send correct password
    data = s.recv(1024).decode()
    print(data)
    encoded_msg = input('Type the correct password...')
    s.send(str.encode(encoded_msg))
    feedback = s.recv(1024).decode()
    print(feedback)
except:
    print('Error...')
finally:
    s.close()