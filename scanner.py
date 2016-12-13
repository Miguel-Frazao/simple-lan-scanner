import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("gmail.com",80))
host = s.getsockname()[0]
s.close()

param = host.split('.')[-2] # getting the octet before the last one
for i in range(255):
	try:
		found = socket.gethostbyaddr('192.168.{}.{}'.format(param, i))
	except Exception as err:
		continue
	print('[+] {}'.format(found))
