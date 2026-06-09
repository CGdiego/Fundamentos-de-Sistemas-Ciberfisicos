from machine import Pin
from utime import sleep

print("Hello, ESP32!")

led = Pin(15, Pin.OUT)
led2 = Pin(2, Pin.OUT)
# enable internal pull-up resistor
btn = Pin(13, Pin.IN, Pin.PULL_DOWN)
switch = Pin(12, Pin.IN)

while True:

    if btn.value() == 0:
        led.on()
    else:
        led.off()

    if switch.value() == 0:
        led2.on()
    else:
        led2.off()