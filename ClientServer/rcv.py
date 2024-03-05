import socket

# Multicast group address and port
MULTICAST_GROUP = '224.1.1.1'
MULTICAST_PORT = 5000

# Create a UDP socket
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
receiver_socket.bind(('', MULTICAST_PORT))

# Set up the socket for multicast
receiver_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MULTICAST_GROUP) + socket.inet_aton('0.0.0.0'))

# Receive multicast messages
while True:
    data, addr = receiver_socket.recvfrom(1024)
    print(f"Received from {addr}: {data.decode('utf-8')}")

