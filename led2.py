import RPi.GPIO as GPIO

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def main():
	try:

		while True:

			GPIO.output(LED_PIN, GPIO.HIGH)

	except Exception as e:

		GPIO.output(LED_PIN, GPIO.LOW)
		GPIO.cleanup()



main()
