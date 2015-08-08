from Tkinter import*
import tkMessageBox
import random
import pygame, sys
from voice import readOut
from pygame.locals import *
from time import sleep
from gattlib import GATTRequester, GATTResponse
import time
from random import randint
req = GATTRequester("EA:02:7F:9E:5F:7C", False)

def problem1():
	tkMessageBox.showinfo("Error", "Unable to connect. Try resetting and restarting.")
def instructions():
    tkMessageBox.showinfo( "INSTRUCTIONS", "Click the left pad when shown on screen.                                            Click the right pad when shown on screen")
def test():
	global top

def initialize():
	try:
	    req.connect(True)
	    req.disconnect()
	    print "connected"
	    return True
	except:
		print "Error connecting"
		try:
		    print "disconnect "
		    req.disconnect()
		except Exception, e:
		    pass
        return False

def trials():
	for i in range(20):
		if(i%2):
			# readOut("press right")
			button_l = Button(None, text = "PRESS LEFT",font=("Helvetica",24,"bold"), command = None, anchor = W)
			button_l.configure(width = 20, activebackground = "black", bg="black",relief = FLAT)
			button_r = Button(None, text = "PRESS RIGHT",font=("Helvetica",24,"bold"), command = None, anchor = W)
			button_r.configure(width = 20, activebackground = "blue", bg="blue",relief = FLAT)
			if not req.is_connected():
				req.connect(True)
				response = GATTResponse()   
				print response
				# print str(ord(response.received()[-1]))
			# readOut("press right")
		else:
			# readOut("press left")
			button_l = Button(None, text = "PRESS LEFT",font=("Helvetica",24,"bold"), command = None, anchor = W)
			button_l.configure(width = 20, activebackground = "blue", bg="blue",relief = FLAT)
			button_r = Button(None, text = "PRESS RIGHT",font=("Helvetica",24,"bold"), command = None, anchor = W)
			button_r.configure(width = 20, activebackground = "black", bg="black",relief = FLAT)


	button_l_window = C.create_window(200, 500, anchor=NW, window=button_l)
	button_r_window = C.create_window(900, 500, anchor=NW, window=button_r)
		

top=Tk()
C = Canvas(top, bg="#fa877a", height=840, width=1600)
C.pack(side="top", fill="both", expand=True)
canvas_id = C.create_text(600, 20, anchor="nw")
C.itemconfig(canvas_id, text="TUTORIAL",font=("Helvetica",48,"bold"))
C.grid()

if(initialize()):
	button4 = Button(None, text = "       CONNECTED",font=("Helvetica",24,"bold"), command = None, anchor = W)
	button4.configure(width = 20, activebackground = "green", bg="green",relief = FLAT)	

else:
	button4 = Button(None, text = "        DISCONNECTED",font=("Helvetica",24,"bold"), command =problem1 , anchor = W)
	button4.configure(width = 20, activebackground = "red", bg="red",relief = FLAT)

button4_window = C.create_window(580,180,anchor=NW, window=button4)

button_ins = Button(None, text = "    INSTRUCTIONS",font=("Helvetica",24,"bold"), command = instructions, anchor = W)
button_ins.configure(width = 20, activebackground = "#ffc100", bg="red",relief = FLAT)
button_ins_window = C.create_window(580, 320, anchor=NW, window=button_ins)

button3 = Button(None, text = "EXIT",font=("Helvetica",24,"bold"), command = top.quit, anchor = W)
button3.configure(width = 20, activebackground = "#ffc100", bg="red",relief = FLAT)
button3_window = C.create_window(580, 700, anchor=NW, window=button3)






# buttonQuestion = Button(None, text = "Question",font=("Helvetica",24,"bold"), anchor = W)
# buttonQuestion.configure(width = 80, activebackground = "#ff6666", bg="#ff6666",relief = FLAT)
# buttonQuestion_window = C.create_window(50,450 , anchor=NW, window=buttonQuestion)

# buttonOp1 = Button(None, text = "Option1",font=("Helvetica",24,"bold"), anchor = W)
# buttonOp1.configure(width = 40, activebackground = "#ff9999", bg="#ff9999",relief = FLAT)
# buttonOp1_window = C.create_window(50,510 , anchor=NW, window=buttonOp1)

# buttonOp2 = Button(None, text = "Options2",font=("Helvetica",24,"bold"), anchor = W)
# buttonOp2.configure(width = 39, activebackground = "#ff9999", bg="#ff9999",relief = FLAT)
# buttonOp2_window = C.create_window(790,510 , anchor=NW, window=buttonOp2)

C.pack()	
trials()
top.mainloop()
