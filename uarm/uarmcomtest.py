import serial
import serial.tools.list_ports

print 'hello'

ports = list(serial.tools.list_ports.comports())

print (ports)

for p in ports:
    print (p[1])
    if "Serial" in p[1]:
	    ser = serial.Serial(port=p[0],baudrate=115200)
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')

def run():
    action = "aaa"
    while action != "q":
        print 'select which tone do you want to play ? 1,2,3, q and others for quit'
        action = raw_input("> ")
        if action == "1":
            ser.write('#2 G0 X100 Y100 Z100 F100\n')
        elif action == "2":
            ser.write('#3 M210 F1000 T0.2\n')
        elif action == "3":
            ser.write('#4 G0 X50 Y50 Z100 F100\n')
        else :
            return

run()
