from machine import Pin
from utime import sleep

led0 = Pin(13, Pin.OUT)
led1 = Pin(14, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(15, Pin.OUT)

btn = Pin(27, Pin.IN, Pin.PULL_DOWN)

numero = 0

while True:

    led0.value(numero & 1)
    led1.value((numero >> 1) & 1)
    led2.value((numero >> 2) & 1)
    led3.value((numero >> 3) & 1)

    if btn.value() == 1:
        numero = numero + 1
        sleep(0.2)