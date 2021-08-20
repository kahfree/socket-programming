#!/usr/bin/env python3
#Team_H_Ethan-Caffrey_Corey-Clohessy_David-Ahern_Server-1
import socket

#Define host and port for socket binding
HOST =  '127.0.0.1'
PORT =  56342

#Create socket and give it the alias 's'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	#Bind the socket using the host and port
	s.bind((HOST, PORT))
	#Listen for a client connection
	s.listen()
	while True:
		#Accept client connection and gather information from client
		conn, addr = s.accept()
		#Display information to terminal
		print('Got connection from', addr)
		#Receive data from client and decode it
		data  = conn.recv(1024)
		data = data.decode("utf-8")
		#Display data from client to terminal
		print(addr,'sent the message',repr(data))
		
		#If the user string is not alphabetic, return message
		if not data.isalpha():
			conn.send(b'Name must contain alphabetic characters only')
		#Otherwise, return the user string
		else:
			conn.send(data.encode("utf-8"))
	
		#Close the socket connection
		conn.close()
		
		
		
			
			
	
