#!/usr/bin/env python3
#Team_H_Ethan-Caffrey_Corey-Clohessy_David-Ahern_Client-1
import socket

#Define the host and port for socket connection
HOST = '127.0.0.1'
PORT = 56342
#Take user input for string name
name = input('Enter your name (alphabetic characters only): ')
#Create socket and give it the alias 's'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	#Connect to the server using the host and port
	s.connect((HOST, PORT))
	#Send the encoded string to the server
	s.send(name.encode("utf-8"))
	#Receive the data from the server
	data = s.recv(1024)

#Print out the data the server sent by decoding it to a string
print('The server replied with: ',data.decode("utf-8"))
#Close the socket connection
s.close()

