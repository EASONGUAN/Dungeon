import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

# establish a connection

clientsocket1, addr1 = serversocket.accept()
print("Got a connection from %s" % str(addr1))
clientsocket2, addr2 = serversocket.accept()
print("Got a connection from %s" % str(addr2))

while True:
    # establish a connection

    msg = clientsocket1.recv(1024)
    msg2 = clientsocket2.recv(1024)

    clientsocket2.send(msg)
    clientsocket1.send(msg2)

    #clientsocket.close()