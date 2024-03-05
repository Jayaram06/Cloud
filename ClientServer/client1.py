#mclient
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.11.147.174', 8990))
    print("Connected Successfully to the Server.")
    print('Enter "exit" to exit the chat.\n')

    while True:
        message = input("Client--> ")
        client_socket.sendall(message.encode())
        
        if message == "exit":
            print("--CLIENT EXITED--")
            break
        
        response = client_socket.recv(1024)
        print("Server--> " + response.decode())
        
        if response.decode().strip() == "exit":
            print("--CLIENT EXITED--")
            break

    client_socket.close()

if __name__ == "__main__":
    main()

