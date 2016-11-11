import urllib2
import time
import os
from datetime import datetime
from winnotify import balloon_tip
URL = "http://www.guimp.com/"
URL1 = "http://google.com"

def check(URL):
	try:
		urllib2.urlopen(URL1,timeout=3)
		return "Working"
	except urllib2.URLError:
		return "Not working"
	except Exception as e:
                if str(e) == 'timed out' or e == None:
                        return "Probably working but too slow"
                obj = open("netcheckREPORT.txt",'a')
                obj.write(str(datetime.now()) + " " + str(e) + "\n")
                obj.close()
                return e
print "\t\t\t",
text = "PREPARE TO BE AMAZED!!"
for i in range(len(text)):
        print text[i],
        time.sleep(0.1)

msg = check(URL)
prevMsg = ""
os.system('cls')
while True:
        if prevMsg != msg:
                balloon_tip("NetCheck",msg)
                prevMsg = msg
	print msg
	time.sleep(5)
	print "refreshing..."
	temp = check(URL)
	if msg != temp:
		msg = temp
	os.system('cls')
