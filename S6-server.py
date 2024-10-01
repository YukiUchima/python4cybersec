import socket

# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind, local host at port 9001
host = '127.0.0.1'
port = 9001
s.bind((host, port))
# listen
s.listen()

# accept
try:
    client, addr = s.accept() # waiting for client to connect, before it can trigger the rest of the application

    print(f'Server: Connection received from {addr}...')

# # if server sending
# while True:
#     data = input('Enter a msg: ')
#     client.sendall(str.encode(data))
#     msg = client.recv(1024).decode()
#     if not msg:
#         break
#     print(msg)
# client.close()
# print(f'Server: Connection {addr} was closed...')

# -----------------------------------------------------------------------
# singular operation, we will create a while loop instead to keep running connection    
# data = "This is a test, thank you for connecting to the server"
# client.send(str.encode(data))
# client.close()
# print(f'Connection with {addr} has been closed')
# -----------------------------------------------------------------------
# Assignment - Ask for correct password

    msg = 'Connection established... please enter password to access vault'
    client.send(str.encode(msg))
    password = client.recv(1024).decode()

    if password == 'shimo':
        msg = 'Access Granted... Welcome to the party!'
        client.send(str.encode(msg))
        print(f'Connection was successfully granted to client at {addr}')
    else:
        msg = 'Access denied.'
        client.send(str.encode(msg))
        print('Password invalid, terminated connection. Burn everything!')
except:
    print("error...")
finally:
    client.close()