import socket

for i in range(255):
	try:
		host = socket.gethostbyname(socket.gethostname())
		param = host.split('.')[-1] # getting the octet before the last one
		found = socket.gethostbyaddr('192.168.{}.{}'.format(param, i))
	except Exception as err:
		continue
	print('[+] {}'.format(found))
