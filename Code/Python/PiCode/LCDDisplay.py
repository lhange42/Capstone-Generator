import time
import adafruit_ssd1306
import adafruit_ina260
import board

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
i2c = board.I2C()
RST = 24
ina260 = adafruit_ina260.INA260(i2c) # accelerometer setup
disp = adafruit_ssd1306.SSD1306_I2C(128,64,i2c, addr=0x3d) # dislay setup
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image) # gets drwaing object to draw on image
draw.rectangle((0,0,width,height), outline=0, fill=0) # clears screen

# variables to help drawing
padding = 2
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default()

while True:
    print("Current: %.2f Voltage: %.2f Power:%.2f"
        %(ina260.current, ina260.voltage, ina260.power))
    time.sleep(1)
    draw.text((x,top),"Generator Voltage:", font=font, fill=255) # displays text of " acceleramtor data"
    draw.text((x, top + 10), "Voltage ={0}".format(round(ina260.current / 4, 3)), font=font, fill=255) 
    disp.image(image)
    disp.display()
    draw.rectangle((100, 12, 55, 50), outline=0, fill=0) # prints a black rectangle on the screen that covers the previous display of values
    disp.image(image)
    disp.display()

