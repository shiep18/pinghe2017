import serial
import serial.tools.list_ports
import time

print 'hello'

ports = list(serial.tools.list_ports.comports())

print (ports)

song1 = ['1\n','1\n','5\n','5\n','6\n','6\n','5\n','4\n','4\n','3\n','3\n','2\n','2\n','1\n']
song2 = ['1','2','3','1','1','2','3','1','3','4','5','3','4','5']

for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser = serial.Serial(port= p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port]='/dev/ttymodem542')

def run():
    action = "aaa"
    while action != "q":
        print 'select which tone do you want to play ? 1,2 q and others for quit'
        action = raw_input("> ")
        if action == "1":
            for notes in song1:
#                ser.write('1')
                ser.write(notes)
                ser.flushOutput
                print "send:"+notes
                echonotes="N"
                notesint=1
                echonotesint=1
                while echonotesint != notesint:
                    print "echonotes:"+echonotes
                    print "notes:"+notes
                    notesint=notes
                    echonotesint=echonotes
                    print "echonotesint:"+echonotesint
                    print "notesint:"+notesint
                    echonotes=ser.read()
                print "get:"+echonotes
#                time.sleep(1)
                print "\n"
                print "\n"
        elif action == "2":
            ser.write('2')
        else :
            return

run()
