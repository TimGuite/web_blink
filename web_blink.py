from flask import Flask
from gpiozero import LED

app = Flask(__name__)

# Using all the pins next to each other
# For pinout use: https://pinout.xyz/#
led_1 = LED(17)
led_2 = LED(27)
led_3 = LED(22)

# Start with LEDs off
led_1.off()
led_2.off()
led_3.off()


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/led/<int:number>/<value>")
def control_led(number: int, value: str):
    args = (number, value)
    if args == (1, "on"):
        led_1.on()
        return "You turned LED 1 On"
    elif args == (1, "off"):
        led_1.off()
        return "You turned LED 1 Off"
    if args == (2, "on"):
        led_2.on()
        return "You turned LED 2 On"
    elif args == (2, "off"):
        led_2.off()
        return "You turned LED 2 Off"
    if args == (3, "on"):
        led_3.on()
        return "You turned LED 3 On"
    elif args == (3, "off"):
        led_3.off()
        return "You turned LED 3 Off"
