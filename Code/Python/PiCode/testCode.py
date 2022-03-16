import adafruit_ssd1306
import digitalio
import board
import busio
import time
import adafruit_ina260

i2c = board.I2C()
ina260 = adafruit_ina260.INA260(i2c)

i2c = busio.I2C(board.SCL, board.SDA)
from PIL import Image, ImageDraw, ImageFont
reset_pin = digitalio.DigitalInOut(board.D24) # any pin!
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr = 0x3d, reset=reset_pin)


oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
while True:

    print("Current: %.2f Voltage: %.2f Power:%.2f"# prints the current, voltage, and power
        %(ina260.current, ina260.voltage, ina260.power))
    text = "Voltage:" + str(ina260.current / 4) 
    (font_width, font_height) = font.getsize(text)
    draw.text(
    (0 + 20 , 0 + 20),
    text,
    font=font,
    fill=255,
)# this is all the formatting for the OLED text display. It displays the current/4 because that's the resistors affect
    print(ina260.current)
# Display image
    oled.image(image)
    oled.show()
    time.sleep(1)
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)# clears the Display
    oled.image(image)
    oled.show
