from machine import Pin
import dht
import time

sensor = dht.DHT22(Pin(15))

print("Iniciando leituras do DHT no MicroPython...")

while True:
    try:
        sensor.measure()
        
        temp = sensor.temperature()
        umid = sensor.humidity()
        
        print(f"Temperatura: {temp:.1f}°C")
        print(f"Umidade: {umid:.1f}%")
        print("-" * 20)
        
    except OSError as e:
        print("Falha ao ler o sensor DHT. Verifique os fios.")
        
    time.sleep(2)

# Lucas Maximiano Rodrigues
# Daniel Godri Neto
# Mateus Weiss Medeiros
# Gustavo Gomes Luciano
# Diego Fonseca Soares
# Joao Victor Meiners Barboza

#Fundamentos Ciberfisicos

#Professor Alisson