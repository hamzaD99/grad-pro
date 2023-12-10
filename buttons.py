import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
leftSwitch = GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
rightSwitch = GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
gearSwitch = GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
redLed = GPIO.setup(29, GPIO.OUT)
greenLed = GPIO.setup(31, GPIO.OUT)
buzzer = GPIO.setup(36, GPIO.OUT)
start_time = time.time()
gear_time = 5
try:
    while True:
        if (GPIO.input(15) == GPIO.LOW) or (GPIO.input(16) == GPIO.LOW):
            current_time = time.time()
            diff = int(current_time - start_time)
            print(f"One of steering buttons is not pressed for {diff} seconds")
            if diff >= gear_time:
                if diff % 10 == 0 or diff == gear_time:
                    print("Hamza HEllo")
                GPIO.output(29, 1)
                GPIO.output(31, 1)
        else:
            print("All is fine!")
            GPIO.output(29, 0)
            GPIO.output(31, 0)
            start_time = time.time()


except KeyboardInterrupt:
    GPIO.cleanup()
    print("pins are clean") 
