
import sys
import pyttsx
# import serial
import time
# from gattlib import GATTRequester, GATTResponse
# import time
# from gattlib import GATTRequester
import time
# file1=open("values.txt","rw+")
# file1.truncate()


# file1=open("values.txt","rw+")
# req = GATTRequester("EA:02:7F:9E:5F:7C")
# class GotFunction(GATTResponse):
#     def on_response(self, name):
#         print "got"
#         print name

def initialize():
	engine = pyttsx.init()
	#voices = engine.getProperty('voices')
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-60)
	#for voice in voices:
	voice = engine.getProperty('voice')
	# engine.setProperty('voice', 2)
	# engine.say('Hello!')
	# engine.say('The question for you is')
	# engine.say(k[1])
	# engine.say('Option 1 is:')
	# engine.say(k[2])
	# engine.say('Option 2 is:')
	# engine.say(k[3])
	# engine.say('Touch the correct option')
	engine.runAndWait()



def readOut(str1):
	engine = pyttsx.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-60)
	#for voice in voices:
	voice = engine.getProperty('voice')
	engine.setProperty('voice', 2)
	engine.say(str1)
	engine.runAndWait()


# k=sys.argv;
# init(k)
# req = GATTRequester("EA:02:7F:9E:5F:7C")

# while True:
#     steps = req.read_by_handle(0x000e)
#     if steps==['\x00']:
#     	pass
#     elif steps==['\x01']:
#     	readOut('You touched the correct option')
#     	k=1
#     elif steps==['\x02']:
#     	readOut('You touched the wrong option')
#     	k=2
#     elif steps==['\x03']:
#     	readOut('You touched both options')
#     	k=3
#     file1.write(str(k))
#     time.sleep(0.5)