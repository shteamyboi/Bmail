#Benjamin Nelson
#Encryptor/Decryptor
def ceasar(before, amount):
	beforelist = []
	after = []
	for i in range(0,len(before)-1):
		beforelist.append(ord(before[i]))#converts the beforelist letters to numbers
	for i in range(0,len(beforelist)):
		if beforelist[i] + amount > 122:
			beforelist[i] = beforelist[i] - 26 + amount#if the number corresponds to anything above z, it loops back around
		else:
			beforelist[i] += amount
	for i in range(0,len(beforelist)):
		after.append(chr(beforelist[i]))#makes the numbers = letters
	return ''.join(after)


def invert(username, password):	
	password = list(password)

	newpass = []

	for i in range(0,len(password)):
		newpass.append(chr((122-ord(password[i])+97)))#'inverts' the password with the same method used to invert color
	
	newpass.append(str(ord(username[len(username)-1])-96))#adds the letter value(a = 1, b = 2 ... z =26) to the end of the pre ceasar 
	
	
	
	return newpass
	
