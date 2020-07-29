import socket
try:
	import requests
except ModuleNotFoundError:
	print("looks like you haven't installed requests library")
	print("pip install requests")


# Get private ip

hostName = socket.gethostname()
print('Hostname :',hostName)
ipAddr = socket.gethostbyname(hostName)
print('Private Ip :',ipAddr)


# Get public ip

ipAdd = requests.get('https://api.ipify.org').text
print('Public Ip :',ipAdd)