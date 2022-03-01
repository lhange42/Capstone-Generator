from flask import Flask
import time
import board
import adafruit_ina260
#import vReader.py

app = Flask(__name__)

#i2c = board.I2C()
#ina260 = adafruit_ina260.INA260(i2c)

@app.route("/")
def DisplayVoltage():
    return "Display Voltage"
if __name__ == "__main__":
                  app.run(host="0.0.0.0", port=80)
#while True:
#print("Current: %.2f Voltage: %.2f Power:%.2f"
#        %(ina260.current, ina260.voltage, ina260.power))
#    time.sleep(1)


