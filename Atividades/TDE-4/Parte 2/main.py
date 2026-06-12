from machine import Pin, ADC
import time


pino_analogico = ADC(Pin(32))
pino_analogico2 = ADC(Pin(33))

pino_analogico.atten(ADC.ATTN_11DB)
pino_analogico2.atten(ADC.ATTN_11DB)

print("Hello, ESP32! Começando as leituras...")

while True:
    valor = pino_analogico.read()
    valor2= pino_analogico2.read()
    print(valor, "do Potentiometer")
    print(valor2, "do Slide")
    time.sleep(1) 

# Lucas Maximiano Rodrigues
# Daniel Godri Neto
# Mateus Weiss Medeiros
# Gustavo Gomes Luciano
# Diego Fonseca Soares
# Joao Victor Meiners Barboza

#Fundamentos Ciberfisicos

#Professor Alisson