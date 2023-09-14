import socket
import threading
import tkinter as tk

run = True
sock_list = []

#window = tk.Tk("Message Log")

#def updateGUI(word):
#writeToWindow(word)

#def writeToWindow(word):
#label = tk.Label(window, text=word)
#label.pack()


#Code for the thread that waits for conections
#It's so the main thread doesn't hang and can process messages
def waitForConnection(socket, c_sock_list) -> None:
    sock, sock_info = socket.accept()
    print(f"Connection recieved by {sock_info[0]} on port {sock_info[1]}")
    sock.send(b"username_request")
    username = sock.recv(1024)
    print(f"({username.decode()}) joined the chat")
    c_sock_list.append((sock, sock_info, username.decode()))


#def newClient(client):

def sendToClients(uname, msg):
    fullmsg = b'msg' + uname + b'\x00' + msg
    for c in sock_list:
        c.send(fullmsg)
    pass

#Console & setup
print("==========\nCHET SERVER\n==========")
s_addr = input("Enter the address for this server: ")
s_port = input("Enter the port for this server: ")

#Set up the manager connection
#m_port = input("\nEnter the port for the server manager: ")
#m_password = input("Enter the password for the server manager: ")

#Setup the server socket object
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind((s_addr, int(s_port)))
s_socket.listen(4)

#Start the thread that waits for connections
waiting_thread = threading.Thread(target=waitForConnection,
                                  args=(s_socket, sock_list))
waiting_thread.start()
print("Started waiting for connections...")

while run:
    for c in sock_list:
        data = c[0].recv(1024)
        if data != b'':
            print(f"[{c[2]}] {data.decode()}")
			

waiting_thread.join()
for s in sock_list:
    s[0].close()
s_socket.close()
