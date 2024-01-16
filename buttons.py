import RPi.GPIO as GPIO
import time
import telegram_sender
telegram_sender.sendMessage("HIIIIIIIIIIIIII")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
start_time = time.time()
diff_allowed = 5
try:
    while True:
        if (GPIO.input(15) == GPIO.HIGH) or (GPIO.input(16) == GPIO.HIGH):
            current_time = time.time()
            diff = int(current_time - start_time)
            if (GPIO.input(15) == GPIO.HIGH) and (GPIO.input(16) == GPIO.HIGH):
                print(f"The steering buttons are not pressed!!")
                if diff % 10 == 0:
                    telegram_sender.sendMessage("The driver is not driving safely!")
                GPIO.output(29, 1)
                GPIO.output(36, 1)
                time.sleep(1)
                continue
            print(f"One of steering buttons is not pressed for {diff} seconds")
            if diff >= diff_allowed:
                if diff % 10 == 0:
                    telegram_sender.sendMessage("The driver is not driving safely!")
                GPIO.output(29, 1)
                GPIO.output(36, 1)
        else:
            print("All is fine!")
            GPIO.output(29, 0)
            GPIO.output(36, 0)
            start_time = time.time()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("pins are clean") 
