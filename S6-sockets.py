# Sockets are used in many many many cybersecurity related tasks
# What is a socket:
#   Two computers have their own ip addresses (255.255.255.255 or etc.)
#   They can have their own ports, handling different types of comms
# Socket is a combination of a IP + port => Socket ( Connection )

# Server-Client connection
# Server ->
    # Socket -> socket is created
    # bind -> binding: when application binds to ip address and port
    # listen -> waits for connection
    # accept -> accept connection

# Client ->
    # Socket -> socket created on client side
    # Connect -> connects to server, server must accept to establish connection
    # Send -> 

# Encoding
string_var = "something"

print(type(string_var))

string_var = str.encode(string_var)

print(type(string_var))