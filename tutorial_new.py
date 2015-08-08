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
# req = GATTRequester("EA:02:7F:9E:5F:7C", False)
# req = GATTRequester("EA:02:7F:9E:5F:7C", False)
req = GATTRequester("EC:C7:D5:05:67:BF", False)
response = GATTResponse()   

tried=False
confirmed=False
calibration_flag = 0
training_flag = 0

def problem1():
    global tried,confirmed
    if not (tried):
        if not (confirmed):
            tried=True
            draw()
            top.update_idletasks()
    else:
        tkMessageBox.showinfo("Error", "Unable to connect. Try resetting and restarting.")
def instructions():
    tkMessageBox.showinfo( "INSTRUCTIONS", "Step1: Calibrate the device.     Step2: Train the user for device. ")

def calibration():
    global calibration_flag, button_l, button_r, top, button_calib, req, response   

    if not req.is_connected():
        req.connect(True)
    readOut("Do not touch the pads while calibration is done.")
    button_l.configure(activebackground = "#66cdaa", bg="#66cdaa",fg="#8d0b7b",activeforeground="#8d0b7b",relief = FLAT)
    button_r.configure(activebackground = "#66cdaa", bg="#66cdaa",fg="#8d0b7b",activeforeground="#8d0b7b",relief = FLAT)
    top.update_idletasks()
    time.sleep(2)

    req.write_by_handle(0x0011,str(bytearray([0x01])))
    readOut("Calibrating")
    req.read_by_handle_async(0x000e, response)
    data2 = 0
    while(data2 != 0xff):
        req.read_by_handle_async(0x000e, response)
        if response.received():
            data2 = ord(response.received()[-1])

    button_calib.configure(activebackground = "#66cdaa", bg="#66cdaa",fg="#8d0b7b",activeforeground="#8d0b7b")
    top.update_idletasks()
    readOut("The calibration has been done. You can now use the device.")

def training():
    global button_l, button_r, top, button_train, req, response   
    l_success=False
    r_success=False

    if not req.is_connected():
        req.connect(True)
    
    button_l.configure(bg="black")
    button_r.configure(bg="#1190f0")
    if not req.is_connected():
        req.connect(True)

    readOut("Please press and hold left pad")
    time.sleep(2)
    req.read_by_handle_async(0x000e, response)
    while not response.received():
        pass

    data = ord(response.received()[-1])
    print data
    if data==1:
        button_l.configure(bg="#66cdaa")
        l_success = True
    else:
        button_l.configure(bg="#f27264")
    top.update_idletasks()
    time.sleep(2)

    readOut("Please press and hold right pad")
    time.sleep(2)
    req.read_by_handle_async(0x000e, response)
    while not response.received():
        pass
    data = ord(response.received()[-1])
    print data
    if data==2:
        r_success = True
        button_r.configure(bg="#66cdaa")
    else:
        button_r.configure(bg="#f27264")
    top.update_idletasks()
    time.sleep(2)

    if (l_success and r_success):
        button_train.configure(bg="#66cdaa")
    button_ins.configure(activebackground="#66cdaa", bg="#66cdaa")
    top.update_idletasks()

def test():
    global top

def initialize():
    global connected
    try:
        req.connect(True)
        req.disconnect()
        print "connected"
        return True
        connected=1
    except:
        print "Error connecting"
        try:
            print "disconnect "
            req.disconnect()
        except Exception, e:
            pass
        # connected=0
        return False
        

top=Tk()
w=top.winfo_screenwidth()
h=top.winfo_screenheight()
# w=640
# h=480
C = Canvas(top, bg="#ffffff",width=w,height=h)# height=840, width=1600)
C.pack(side="top", fill="both", expand=True)
canvas_id = C.create_text(600*w/1600, 20*h/840, anchor="nw")
C.itemconfig(canvas_id, text="TUTORIAL",font=("Helvetica",48*w/1600,"bold"))
C.grid()
calibration_flag=0
training_flag=0
# connected=0
connected=0
initialize()
print connected

def draw():
    global button4, tried
    if(initialize()):
        button4 = Button(None, compound=CENTER,text = "   CONNECTED",font=("Helvetica",24*w/1600,"bold"), command = None, anchor = W)
        button4.configure(width = w/100, activebackground = "#66cdaa", bg="#66cdaa",fg="#8d0b7b",activeforeground="#8d0b7b",relief = FLAT)  
    else:
        if not (tried):
            button4 = Button(None, compound=CENTER,text = "   DISCONNECTED",font=("Helvetica",24*w/1600,"bold"), command =problem1 , anchor = W)
            button4.configure(width = w/100, activebackground = "#f27264", bg="#f27264",fg="#066b5e",activeforeground="#066b5e",relief = FLAT)
        else:
            button4 = Button(None, compound=CENTER,text = "   CONNECTING",font=("Helvetica",24*w/1600,"bold"), command =problem1 , anchor = W)
            button4.configure(width = w/100, activebackground = "#f2e17c", bg="#f2e17c",fg="#1748f6",activeforeground="#1748f6",relief = FLAT)
    button4_window = C.create_window(3*w/8 ,180*h/840,anchor=NW, window=button4)
            
draw()




button_ins = Button(None, compound=CENTER,text = "   INSTRUCTIONS",font=("Helvetica",24*w/1600,"bold"), command = instructions, anchor = W)                            
button_ins.configure(width = w/100                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         , activebackground = "#ffc100", bg="#9d26f0",fg="#361612",activeforeground="#361612",relief = FLAT)
button_ins_window = C.create_window(3*w/8, 250*h/840, anchor=NW, window=button_ins)

button3 = Button(None, compound=CENTER,text = "        EXIT",font=("Helvetica",24*w/1600,"bold"), command = top.quit, anchor = W)
button3.configure(width = w/100, activebackground = "#ffc100", bg="#f27264",relief = FLAT)
button3_window = C.create_window(3*w/8, 700*h/840, anchor=NW, window=button3)
print w/8

button_l = Button(None,compound=CENTER, text = "PRESS LEFT",font=("Helvetica",24*h/840,"bold"), command = None, anchor = W)
button_r = Button(None,compound=CENTER, text = "PRESS RIGHT",font=("Helvetica",24*h/840,"bold"), command = None, anchor = W)
button_l_window = C.create_window(w/4, 500*h/840, anchor=NW, window=button_l)
button_r_window = C.create_window(4*w/8, 500*h/840, anchor=NW, window=button_r)
    
button_calib= Button(None, compound=CENTER,text = "   CALIBRATION",font=("Helvetica",24*w/1600,"bold"), command = calibration, anchor = W)
button_calib.configure(width =  w/100, activebackground = "#ffc100", bg="#c50522",relief = FLAT)    
button_calib_window = C.create_window(3*w/8, 320*h/840, anchor=NW, window=button_calib)

button_train = Button(None, compound=CENTER,text = "   TRAINING",font=("Helvetica",24*w/1600,"bold"), command = training, anchor = W)
button_train.configure(width =  w/100, activebackground = "#ffc100", bg="#c50522",relief = FLAT)
button_train_window = C.create_window(3*w/8, 390*h/840, anchor=NW, window=button_train)
        
def start():
    global calibration_flag, training_flag
    if(calibration_flag==1):
        button_calib_window = C.create_window(3*w/8, 320*h/840, anchor=NW, window=button_calib)
    else:
        button_calib= Button(None,compound=CENTER, text = "   CALIBRATION",font=("Helvetica",24*w/1600,"bold"), command = calibration, anchor = W)
        button_calib.configure(width =  w/100, activebackground = "#ffc100", bg="#c50522",relief = FLAT)
        button_calib_window = C.create_window(3*w/8, 320*h/840, anchor=NW, window=button_calib) 
    if(training_flag==1):
        button_calib= Button(None, compound=CENTER,text = "   TRAINING",font=("Helvetica",24*w/1600,"bold"), command = None, anchor = W)
        button_calib.configure(width = w/100, activebackground = "#1a9246", bg="#1a9246",fg="#600746",activeforeground="#600746",relief = FLAT) 
        button_calib_window = C.create_window(3*w/8, 390*h/840, anchor=NW, window=button_calib)
    else:
        button_ins = Button(None, compound=CENTER,text = "   TRAINING",font=("Helvetica",24*w/1600,"bold"), command = training, anchor = W)
        button_ins.configure(width =  w/100, activebackground = "#ffc100", bg="#c50522",relief = FLAT)
        button_ins_window = C.create_window(3*w/8, 390*h/840, anchor=NW, window=button_ins)
    



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
# initialize()
# start()
top.mainloop()
