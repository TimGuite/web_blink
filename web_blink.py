from flask import Flask
from gpiozero import LED

app = Flask(__name__)

led = LED(17)


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/led/<value>")
def control_led(value: str):
    if value == "on":
        led.on()
        return "You turned the LED on"
    elif value == "off":
        led.off()
        return "You turned the LED off"
