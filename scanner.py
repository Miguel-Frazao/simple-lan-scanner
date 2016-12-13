import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("gmail.com",80))
lan_ip, sock_port = s.getsockname() # getting network ip and port... not using port though
s.close()

octets = lan_ip.split('.') # getting the octets
for i in range(255):
	try:
		found = socket.gethostbyaddr('{}.{}.{}.{}'.format(octets[0], octets[1], octets[2], i))
	except Exception as err:
		continue
	print('[+] {}'.format(found))
