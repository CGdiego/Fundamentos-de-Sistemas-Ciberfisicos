from machine import Pin
from utime import sleep

print("Hello, ESP32!")

resposta = input("Oi, tudo bem? ")

print(resposta)

led = Pin(15, Pin.OUT)
led2 = Pin(2, Pin.OUT)
while True:
  led.on()
  led2.off()
  sleep(0.5)
  led.off()
  led2.on()
  sleep(0.5)
