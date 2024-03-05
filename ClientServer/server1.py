#mserver
import socket
import threading

def handle_client(client_socket):
    print("Client connected. Thread created.")
    while True:
        data = client_socket.recv(1020)
        print("Client--> " + data.decode())
        message = input("Server--> ") + "\n"
        client_socket.send(message.encode())
        if data.decode().strip() == "exit":
            print("Client disconnected. Thread closed.")
            break
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 8081))
    server_socket.listen(10)
    print("Socket Binded and Listening.")

    threads = []

    for _ in range(10):
        client_socket, _ = server_socket.accept()
        print("Server Accepted a Client.")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    server_socket.close()

if __name__ == "__main__":
    main()

