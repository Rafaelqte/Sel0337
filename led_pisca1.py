import RPi.GPIO as GPIO
import time

LED_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def main ():
	try:
		while True:
			GPIO.output(LED_PIN, GPIO.HIGH)
			time.sleep(2)
			GPIO.output(LED_PIN, GPIO.LOW)
			time.sleep(2)



	finally:
		GPIO.cleanup()

main()
