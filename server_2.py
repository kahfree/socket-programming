#!/usr/bin/env python3
#Team_H_Ethan-Caffrey_Corey-Clohessy_David-Ahern_Server-2
import socket
#Define host and port for socket binding
HOST =  '127.0.0.1'
PORT =  55443

separator = ','

#Define the power of two function for use on client number set
def powerOfTwo(n):
	if not n == 0 and not n & (n-1):
		return True
	else:
		return False

#Create socket and use alias 's'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	while True:
		conn, addr = s.accept()
		print('Got connection from', addr)
		
		#Receive message from client
		clientmessage  = conn.recv(1024)
		
		#Convert it to string from bytes object
		clientmessage = clientmessage.decode("utf-8")
		
		#Convert into string list from string
		clientmessage = clientmessage.split(separator)
		
		#Convert into int list from string list
		numbers_map = map(int, clientmessage)
		numbers = list(numbers_map)
		
		#Create string to return to client
		data_list = []
		for n in numbers:
			data_list.append(str(powerOfTwo(n)))
		#Convert the results from the power of two functions into a string 
		data = separator.join(data_list)
		#Encode the string and send it to the client
		conn.send(data.encode("utf-8"))
	
		#Close the socket connection
		conn.close()
