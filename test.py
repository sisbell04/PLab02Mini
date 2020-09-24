from threading import Thread
import RPi.GPIO as GPIO
from time import sleep

class Actuator1:
    def __init__(self):
        self.stopped = False
        self.GPON = False
        self.timming = 0.5
        self.outPort = 23
        self.n = 0

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(outPort, GPIO.OUT)
        while(True):
            if(self.stopped):
                return
            GPIO.output(outPort, GPON)
            sleep(0.5)
            GPON = not GPON
    
    def stop(self):
        self.stopped = True
    def setTime(self):
        self.timming = self.timming + 0.1
    def setOut(self):
        n = n+1
        if(n > 2):
            n = 0
            outport = 23
        if(n == 1):
            outport = 24
        if(n == 2):
            outport = 25

greenLight = Actuator1()
yellowLight = Actuator1()
yellowLight.setOut()
redLight = Actuator1()
redLight.setTime()
redLight.setOut()
redLight.setOut()

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