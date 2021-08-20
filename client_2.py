#!/usr/bin/env python3
#Team_H_Ethan-Caffrey_Corey-Clohessy_David-Ahern_Client-2
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
		

