import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class PWMchanged(GPIO.PWM):
    def __init__(self, chan, freq):
        super().__init__(chan, freq)
        self.start(freq)
    def duty(self,dutycycle): self.ChangeDutyCycle(dutycycle/65535)
    def freq(self, value): self.ChangeFrequency(value)
    def deinit(self): self.stop()
    pass

def PWM(pin):
    GPIO.setup(pin, GPIO.OUT) # Just to make sure
    return PWMchanged(pin, 50) # 50

def Pin(pin):
    GPIO.setup(pin, GPIO.OUT)
    return pin
