import socket
import threading

run = True

def waitForConnection(socket, glob_socket) -> str:
    sock, sock_info = socket.accept()
    glob_socket = sock
    return f"Connection recieved by {sock_info[0]} on port {sock_info[1]}"



#Console & setup
print("==========\nCHET SERVER\n==========")
this_addr = input("Enter the address for this server: ")
this_port = input("Enter the port for this server: ")

#Setup the server socket object
this_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
this_socket.bind((this_addr, this_port))
this_socket.listen(4)

#Start the thread that waits for connections
waiting_thread = threading.Thread(target=waitForConnection)
waiting_thread.start()
print("Started waiting for connections...")


while run:
    pass