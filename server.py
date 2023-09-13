import socket
import threading

run = True
sock_list = []


#Code for the thread that waits for conections
#It's so the main thread doesn't hang and can process messages
def waitForConnection(socket, c_sock_list) -> None:
    sock, sock_info = socket.accept()
    c_sock_list.append((sock, sock_info))
    print(f"Connection recieved by {sock_info[0]} on port {sock_info[1]}")
    
#def newClient(client):



#Console & setup
print("==========\nCHET SERVER\n==========")
s_addr = input("Enter the address for this server: ")
s_port = input("Enter the port for this server: ")

#Setup the server socket object
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind((s_addr, int(s_port)))
s_socket.listen(4)

#Start the thread that waits for connections
waiting_thread = threading.Thread(target=waitForConnection, args=(s_socket, sock_list))
waiting_thread.start()
print("Started waiting for connections...")


while run:
    for c in sock_list:
        data = c[0].recv(1024)
        if data != b'':
            print(f"{c[1]} {data.decode()}")
        


waiting_thread.join()
for s in sock_list:
    s[0].close()
s_socket.close()
