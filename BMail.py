#Benjamin Nelson
#BMail
#Email Client
import crypto
import login
import os
import getpass#Mr Morse told me about this module
import time
import makedir

def main():
	makedir.makedir("Accounts")
	os.chdir("Accounts")
	
	os.system('clear')
	error = True
	while error:

		create = input("create a new account or login to an existing acount(create/login) > ")
		if create.lower() == "create" or create.lower() == "login":
			error = False
		else:
			print('incorrect selection, please try again')

	if create == "create":
		username = input('username > ')
		login.creation(username)
		doquit = input('quit? (y/n) > ')
		if doquit.lower() == 'y':
			exit()
		elif doquit.lower() == 'n':
			create = input("create a new account or login to an existing acount(create/login) > ")
						
	if create == "login":	
		username = input('username > ')	
		loggedin = login.logged(username)
		
		if loggedin:
			os.system('clear')
			print('logged in')
			time.sleep(0.5)
			os.system('clear')
			
			while True:
				print("1: Check Mailbox")
				print("2: Compose Mail")
				print("3: Create Mailbox")
				print("4: Delete Mail")
				print("5: Mark Spam")
				print("6: Logout\n")
				choice = input('> ')
				
				try:
					int(choice)
					
					if int(choice) == 1:
						print("==================")
						directory = []
						for i in range(0,len(os.listdir())):
							if os.listdir()[i] != username+'pass.txt':
								directory.append(os.listdir()[i])
						for i in range(len(os.listdir())-1,0,-1):
							print('\n'+os.listdir()[i]+'\n')
						print("==================\n")
						choice = input('\nread which category?\n> ')
						for i in range(0,len(os.listdir())):
							if os.listdir()[i] == choice:
								print(choice+' selected')
								os.chdir(choice)
								print(os.listdir())
					elif int(choice) == 6:
						exit()
				
				
				except Exception:
					print("please try again")
					os.system("clear")

if __name__ == '__main__':
	main()
