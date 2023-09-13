import socket

print("===========\nCHET CLIENT\n===========")

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_address = input("Enter the address of the server: ")
s_port = input("Enter the port of the server: ")
c_socket.connect((s_address, int(s_port)))
print("Enter messages:")
while True:
    message = input()
    
    if message == "terminate":
        c_socket.send(b"Disconnecting from server")
        break
    else:
        c_socket.send(message.encode())

c_socket.close()




