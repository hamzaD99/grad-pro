import RPi.GPIO as GPIO
import time
import telegram_sender

start_time = time.time()
sent = False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
greenLed = GPIO.setup(31, GPIO.OUT)
GPIO.output(31, 0)

while True:
    current_time = time.time()
    diff = int(current_time - start_time)
    if diff >= 5:
    # if diff >= 28800:
        GPIO.output(31, 1)
        if not sent:
            print("Your shift is over!")
            telegram_sender.sendMessage("Your shift is over!")
            sent = True