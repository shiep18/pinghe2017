import serial

print 'hello'

ports = list(serial.tools.list_ports.comports())

print (ports)
for p in ports:
    print (p[1])
    if "CH340" in p[1]:
	    ser = serial.Serial(port= p[0])
        print 'open serial'
        print p[0]
    else:
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')

def run():
    action = "aaa"
    while action != "q":
        print 'select which tone do you want to play ? 1,2 q and others for quit'
        action = raw_input("> ")
        if action == "1":
            ser.write('1')
        elif action == "2":
            ser.write('2')
        else :
            return

run()
