import socket

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('',port))
print("socket is binded to %s" %(port))

s.listen(5)
print("socket is listening")

while True:
	c,addr = s.accept()
	print('Got connection from',addr)
	c.send("thank you for connecting".encode())
	c.close()
	break
	
