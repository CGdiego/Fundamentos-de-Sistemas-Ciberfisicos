from machine import Pin, I2C
import ssd1306

# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Lucas', 0, 0)  
oled.text('Daniel', 65, 0)
oled.text('Mateus', 0, 11)
oled.text('Gustavo', 65, 11)
oled.text('Diego', 0, 22)
oled.text('Joao', 65, 22)

oled.text('Fundamentos', 0, 35) 
oled.text('Ciberfisicos', 0, 43) 

oled.text('Alisson', 0, 57)

oled.show()