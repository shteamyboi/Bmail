from email.mime.text import MIMEText
from subprocess import Popen, PIPE

def mailme(whatfile,subject):

	textfile = str(whatfile)+".txt"
	me = "noreply"
	you = ["pythonscriptautosend@gmail.com"]	
	
	#open the message file
	#the text file can only have ASCII characters
	with open(textfile, 'r') as fp:
		#format the message
		msg = MIMEText(fp.read())


	msg['Subject'] = subject
	msg['From'] = me
	msg['To'] = ', '.join(you)
	
	
	p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
	p.communicate(str(msg).encode())#the message needs to be encoded and MIMEText can't be encoded, .encode() was found here https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-writing-to-a-file-in

mailme('mail','local web server')
