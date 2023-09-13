import socket
import threading

msgSend = True


#Function that listens for requests from the server
def listenToServer(client):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
			msgSend = False
            serverRequest(data)
			msgSend = True
        except Exception as e:
            print(f"Server request error: {str(e)}")
            break


def serverRequest(request):
    if request == b"username_request":
        c_socket.send(username.encode())


print("===========\nCHET CLIENT\n===========")

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_address = input("Enter the address of the server: ")
s_port = input("Enter the port of the server: ")
username = input("Enter a username: ")
print("Press enter to attempt a connection")
input()
c_socket.connect((s_address, int(s_port)))

#Set up the thread that listens for server requests
listeningThread = threading.Thread(target=listenToServer, args=(c_socket))
listeningThread.start()


print("Enter messages:")
while True:
    if msgSend:
        message = input()

        if message == "terminate" && msgSend:
            c_socket.send(b"Disconnecting from server")
            break
        else:
            c_socket.send(message.encode())

c_socket.close()
