#intro_to_sockets
import socket
import sys
#sock = socket.gethostbyname('www.backtrackacademy.com')
#print(sock)

# obtiene el puerto:
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.bind(('0.0.0.0', 0))
#print('listening on port:', sock.getsockname()[1])
#----------------------------------------

# Enviando datos al servidor destino
'''
TCP_IP = '127.0.0.1'
TCP_PORT = 8000
MESSAGE_TO_SERVER = b"Hello, World!"
BUFFER_SIZE = 1024 #Normally use 1024, to get fast response from the server use small size
try:
	#Create an AF_INET (IPv4), STREAM socket (TCP)
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
	print('Error occurred while creating socket. Error code: ' + str(e[0])+ ' , Error message : ' + e[1])
	sys.exit();
tcp_socket.connect((TCP_IP, TCP_PORT))
try :
#Sending message
	tcp_socket.send(MESSAGE_TO_SERVER)
except socket.error as e:
	print('Error occurred while sending data to server. Error code: ' +str(e[0]) + ' , Error message : ' + e[1])
	sys.exit()
print('Message to the server send successfully')
print(MESSAGE_TO_SERVER)
'''
#---------------------------------------------
# Recibir datos del servidor
TCP_IP = '127.0.0.1'
TCP_PORT = 8000
BUFFER_SIZE = 1024 #Normally use 1024, to get fast response from the server use small size
try:
#Create an AF_INET (IPv4), STREAM socket (TCP)
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
	print('Error occurred while creating socket. Error code: ' + str(e[0]) +
	' , Error message : ' + e[1])
	sys.exit();
try:
	tcp_socket.bind((TCP_IP, TCP_PORT))
except socket.error as e:
	print('Error occurred while sending data to server. Error code: ' +str(e))
	sys.exit()
# Listen for incoming connections (max queued connections: 2)
tcp_socket.listen(2)
print('Listening..')
#Waits for incoming connection (blocking call)
connection, address = tcp_socket.accept()
print('Connected with:', address)
#---------------------------------------------------
