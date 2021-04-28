from flask import Flask, render_template, jsonify
from gpiozero import LED

app = Flask(__name__)

# Using all the pins next to each other
# For pinout use: https://pinout.xyz/#
red_led = LED(17)
green_led = LED(27)
blue_led = LED(22)

# Start with LEDs off
red_led.off()
green_led.off()
blue_led.off()


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/led/<int:number>/<value>")
def control_led(number: int, value: str):
    args = (number, value)
    if args == (1, "on"):
        red_led.on()
        return "You turned LED 1 On"
    elif args == (1, "off"):
        red_led.off()
        return "You turned LED 1 Off"
    if args == (2, "on"):
        green_led.on()
        return "You turned LED 2 On"
    elif args == (2, "off"):
        green_led.off()
        return "You turned LED 2 Off"
    if args == (3, "on"):
        blue_led.on()
        return "You turned LED 3 On"
    elif args == (3, "off"):
        blue_led.off()
        return "You turned LED 3 Off"


@app.route("/status/")
def status():
    response = {
        "red": red_led.value,
        "green": green_led.value,
        "blue": blue_led.value
    }
    return jsonify(response)
