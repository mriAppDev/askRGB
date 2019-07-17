# askRGB.py created by JC Irvine

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

rgbGo = 1

print ("Starting RBG light tester")
while rgbGo == 1:

        choice = raw_input("Which color shall be lit? 'R,G,or B'?")
        print ("You chose "+choice)

        if choice == "R":
                GPIO.output(18, True)
                time.sleep(5)
                GPIO.output(18, False)

        elif choice == "G":
                GPIO.output(23, True)
                time.sleep(5)
                GPIO.output(23, False)

        elif choice == "B":
                GPIO.output(24, True)
                time.sleep(5)
                GPIO.output(24, False)
        else:
                print("All done then... OK :) ")
                rgbGo = 0

GPIO.cleanup()