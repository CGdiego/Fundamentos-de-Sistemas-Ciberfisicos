from machine import Pin
from utime import sleep

led0 = Pin(15, Pin.OUT)
led1 = Pin(12, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
while True:
    for numero in range(16):
        led0.value(numero & 1)         # bit 0
        led1.value((numero >> 1) & 1)  # bit 1
        led2.value((numero >> 2) & 1)  # bit 2
        led3.value((numero >> 3) & 1)  # bit 3
        sleep(0.5)