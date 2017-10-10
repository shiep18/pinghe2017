import serial
import time

print 'hello'

ser=serial.Serial(port='COM4')

time.sleep(2)

n=ser.write('1')
n=ser.write('2')
n=ser.write('3')


print 'after write'
print n

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
