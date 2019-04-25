#Benjamin Nelson
#makedir
import os

def makedir(folder):
	containstest = 0
	for i in range(0,len(os.listdir())):#if the folder doesn't already exist, create it
		if os.listdir()[i] == folder:
			containstest += 1
	if containstest == 0:
		os.mkdir(folder)
