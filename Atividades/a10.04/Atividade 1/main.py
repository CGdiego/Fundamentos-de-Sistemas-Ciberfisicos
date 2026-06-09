from machine import Pin
from utime import sleep

print("Hello, ESP32!")

led = Pin(15, Pin.OUT)
# enable internal pull-up resistor
btn = Pin(12, Pin.IN, Pin.PULL_UP)

while True:


    if btn.value() == 0:
        led.on()
    else:
        led.off()