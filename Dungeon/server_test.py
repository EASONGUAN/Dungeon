import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.settimeout(0.00000000000000000001)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

# establish a connection
'''
clientsocket1, addr1 = serversocket.accept()
print("Got a connection from %s" % str(addr1))
clientsocket2, addr2 = serversocket.accept()
print("Got a connection from %s" % str(addr2))
clientsocket1.send("connected!".encode('ascii'))
'''

socket_list =[]
pairs = []

while True:
    # establish a connection
    try:
        newclient, newaddr = serversocket.accept()
        print("Got a connection from %s" % str(newaddr))

    except:
        pass

    else:
        socket_list.append(newclient)
        #print(socket_list)
        added = False
        for pair in pairs:
            if not pair[1]:
                pair[1] = newclient
                added = True
                pair[0].send('Paired!'.encode('ascii'))
                pair[1].send('Paired!'.encode('ascii'))
                break
        if not added:
            pairs.append([newclient, None])

    for pair in pairs:
        #print(pairs)
        if pair[1] != None:
            player1 = pair[0]
            player2 = pair[1]
            msg = player1.recv(4096)
            msg2 = player2.recv(4096)
            player2.send(msg)
            player1.send(msg2)
        #print('ggggg')

    #clientsocket.close()