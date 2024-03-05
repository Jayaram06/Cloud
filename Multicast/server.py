import socket
import struct

# Multicast group and port
MULTICAST_GROUP = '224.1.1.1'
PORT = 5000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the time-to-live for messages
ttl = struct.pack('b', 1)  # TTL of 1
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Send data to the multicast group
while True:
    message = input("Enter message to multicast: ")
    sock.sendto(message.encode(), (MULTICAST_GROUP, PORT))

# Close the socket
sock.close()

