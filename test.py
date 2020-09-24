from threading import Thread
import RPi.GPIO as GPIO
from time import sleep

class Actuator1:
    def __init__(self):
        self.stopped = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        self.GPON = False
        self.timming = 0.5

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        while(True):
            if(self.stopped):
                return
            GPIO.output(23, GPON)
            sleep(0.5)
            GPON = not GPON
    
    def stop(self):
        self.stopped = True
    def setTime(self):
        self.timming = self.timming + 0.1

greenLight = Actuator1()
yellowLight = Actuator1()
redLight = Actuator1()
redLight.setTime()

def main():
    greenLight.start()
    yellowLight.start()
    redLight.start()
    stopTimer = 20
    while(stopTimer > 0):
        stopTimer = stopTimer - 1
        sleep(1)
    greenLight.stop()
    yellowLight.stop()
    redLight.stop()
    exit()
    
if __name__ == "__main__":
    main()