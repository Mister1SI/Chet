import socket
import threading

run = True

#Code for the thread that waits for conections
#It's so the main thread doesn't hang and can process messages
def waitForConnection(socket, glob_socket) -> str:
    sock, sock_info = socket.accept()
    glob_socket = sock
    return f"Connection recieved by {sock_info[0]} on port {sock_info[1]}"



#Console & setup
print("==========\nCHET SERVER\n==========")
s_addr = input("Enter the address for this server: ")
s_port = input("Enter the port for this server: ")

#Setup the server socket object
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind((s_addr, int(s_port)))
s_socket.listen(4)

#Start the thread that waits for connections
waiting_thread = threading.Thread(target=waitForConnection)
waiting_thread.start()
print("Started waiting for connections...")


while run:
    pass


waiting_thread.join()


