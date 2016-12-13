import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("gmail.com",80))
host = s.getsockname()[0] # getting network ip
s.close()

octets = host.split('.') # getting the octet before the last one
for i in range(255):
	try:
		found = socket.gethostbyaddr('{}.{}.{}.{}'.format(octets[0], octets[1], octets[2], i))
	except Exception as err:
		continue
	print('[+] {}'.format(found))
