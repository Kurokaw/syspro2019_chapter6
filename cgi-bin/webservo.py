#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('<input type="number" name="number">')
print('<input type="submit" value="move!">')
print('</form>')


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

#y = (4.75/90)x + 7.25
def setservo(x):
	if x>90:
		servo.ChangeDutyCycle(top)
	elif x<-90:
		servo.ChangeDutyCycle(bottom)
	else :
		servo.ChangeDutyCycle((4.75/90)*x+7.25)

form = cgi.FieldStorage()
value = form.getvalue("number")
print(value)
print(float(value))
setservo(float(value))
