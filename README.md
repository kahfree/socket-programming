# socket-programming
This project was created for my 'Internetworking' Class. The project required me to write python code for a client and a server and have them interact. I found this process enjoyable to learn because I had wrote basic programs in python before but this was more specifically using the socket library and in turn became a whole new bit to learn. 
Watching the client interact with the server and knowing how I got them to interact and work with one another made it easier for me to understand how to interactions just like this (albeit on a much larger scale) happen on the internet all the time.

## Client-Server 1 (Echo Server)
This first client-server I had to create was the ability for a client to send a string to a server, and granted it was alphabetic characters only the server would reply with the same message the client sent. Otherwise it would throw an error.
#### The Client Code
```Python
#!/usr/bin/env python3
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
```
#### The Server Code
```Python
#!/usr/bin/env python3
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
```

## Client-Server 2 (Power of Two Check)
this Client-Server allows the client to enter up to 4 numbers and then the server will check if each of these numbers are a power of two.
#### The Client Code
```Python
#!/usr/bin/env python3

import socket

#Define host and port for socket connection
HOST = '127.0.0.1'
PORT = 55443

#Define variables used to gather user input
userinput = 0
numbers_list = []
#Collect the users numbers
print('Enter up to 4 numbers!' '(type "break" to end input early)')
#Gather maximum of 4 numbers, so for loop is max 4 iterations
for i in range(4):
	#Prompt user and receive input
	userinput = input("Enter number " + str(i+1) + ": ")
	#Check if the input is a valid number
	if userinput.isnumeric():
		numbers_list.append(userinput)
	elif userinput == 'break':
		break
	else:
		print("input must be numeric or keyword 'break'")
		
separator = ','
#Convert list into string for sending
stringOfNumbers = separator.join(numbers_list)

#Make socket connection to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	#Convert string to bytes object and send to server
	s.send(stringOfNumbers.encode("utf-8"))
	#Receive the message from the server
	data = s.recv(1024)
	#Convert bytes object into string
	data = data.decode("utf-8")
	#Convert bytes object into list
	data_list = data.split(separator)
	#Iterate for a many items as there are in the server message
	for i in range(0,len(data_list)):
		if data_list[i] == 'True':
			print("The number",numbers_list[i],"is a power of two!")
		else:
			print("The number",numbers_list[i],"is not a power of two.")

	s.close()
```
#### The Server Code
```Python
#!/usr/bin/env python3

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
````
