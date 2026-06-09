from machine import Pin
from utime import sleep

print("Hello, ESP32!")

led = Pin(15, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(14, Pin.OUT)
while True:
  led.on()
  led2.off()
  led3.off()
  sleep(0.5)
  led.off()
  led2.on()
  led3.off()
  sleep(0.5)
  led.off()
  led2.off()
  led3.on()
  sleep(0.5)