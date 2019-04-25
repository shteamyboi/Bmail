#Benjamin Nelson
#Login


import crypto
import login
import os
import getpass#Mr Morse told me about this module
import time
import makedir


def login(username, password, createOrCheck):

	inverted = crypto.invert(username, password)
	
	after = list(crypto.ceasar(inverted,ord(username[-1])-97))
	
	after.append("~")
	if inverted[-2] == "1" or inverted[-2] == "2":#adds an escape character, ~ so that the decryptor knows how much to reverse the ceasar cypher
		after.append(inverted[-2])
	after.append(inverted[-1])
	if createOrCheck.lower() == "create":
		if username != "admin":
			makedir.makedir(username)#admin doesn't get a folder, it has access to all account's emails
			os.chdir(username)
			makedir.makedir("inbox")
			makedir.makedir("spam")
			makedir.makedir("trashes")
	
		with open(username+"pass.txt","w") as w:#opens the password file in the username folder, either writes the new password or
			w.write(''.join(after))				#checks the existing one
	if createOrCheck.lower() == "check":
		if username != 'admin':
			os.chdir(username)
		with open(username+"pass.txt","r") as r:
			passhash = r.readline()
			if passhash == ''.join(after):#if the password entered is the same as the stored password, access is granted
				unlock = True
				return unlock
	os.chdir('..')
def creation(username):
	error = True
		
	while error:
		has = 0
		for i in range(0,len(os.listdir())):
			if os.listdir()[i] == username:#if the username matches a folder or the admin's password file, you have to try again
				has += 1
			if os.listdir()[i] == 'adminpass.txt' and username == "admin":
				has += 1
				
		if has == 0:
			error = False
		elif has >= 1:
			print("user already exists")
	error = True
	while error:		
		password = getpass.getpass('password > ')
		againpass = getpass.getpass("confirm password > ")#you have to confirm your password if you're making a new one
		
		if password == againpass:
			login(username, password, "create")#if the passwords match, the program moves on
			error = False
		elif password != againpass:
			print("\nsomething went wrong, please try again\n")#you have to enter your password until you get it
			password = getpass.getpass("password > ")
			againpass = getpass.getpass("confirm password > ")
def logged(username):
	if username == 'exit':
		exit()
	if username != 'admin':
		error = True
		while error:
			counter = 0
			for i in range(0,len(os.listdir())):
				if os.listdir()[i] == username:
					counter += 1
					error = False
			if counter == 0:
				print(os.listdir())
				print('invalid username')
				os.listdir()
	password = getpass.getpass("password > ")
				
	logged = login(username, password, "check")
	return logged
