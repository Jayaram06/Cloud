import socket

# Multicast group and port
MULTICAST_GROUP = '224.1.1.1'
PORT = 5000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
sock.bind(('', PORT))

# Tell the operating system to add the socket to the multicast group on all interfaces.
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MULTICAST_GROUP) + socket.inet_aton('0.0.0.0'))

# Receive/respond loop
while True:
    data, address = sock.recvfrom(1024)
    print(f"Received message: {data.decode()} from {address}")

# Close the socket
sock.close()

