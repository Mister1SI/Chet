import socket
import threading
import tkinter as tk

msgSend = True

# Function that listens for requests from the server
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
    text = request.decode()
    if text == "username_request":
        c_socket.send(username.encode())
        winprint("Successfully connected to the server")
    elif text.startswith("msg"):
        nullindex = text.find('\x00')
        if nullindex != -1:
            uname = text[3:nullindex]
            msg = text[nullindex + 1:]
            # Now you can use uname and msg as needed
            winprint(f"Received message from {uname}: {msg}")


# Function to print messages in the tkinter window
def winprint(msg):
    msgbox.insert(tk.END, msg + '\n')
    msgbox.see(tk.END)  # Automatically scroll to the end

print("===========\nCHET CLIENT\n===========")

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_address = input("Enter the address of the server: ")
s_port = input("Enter the port of the server: ")
username = input("Enter a username: ")
print("Press enter to attempt a connection")
input()
c_socket.connect((s_address, int(s_port)))

# Set up the thread that listens for server requests
listeningThread = threading.Thread(target=listenToServer, args=(c_socket,))
listeningThread.start()

# Set up the client window
c_window = tk.Tk()
c_window.title("Chet Client")
msgbox = tk.Text(c_window, height=10, width=40)
msgbox.pack()

# Entry for user messages
entry = tk.Entry(c_window)
entry.pack()

def send_message(event):
    global msgSend
    if msgSend:
        message = entry.get()
        entry.delete(0, tk.END)

        if message == "terminate" and msgSend:
            c_socket.send(b"Disconnecting from server")
        else:
            c_socket.send(message.encode())

# Bind the Enter key to send messages
entry.bind("<Return>", send_message)

c_window.mainloop()

# Close the socket when the GUI is closed
c_socket.close()
