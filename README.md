# Present In 10 Demo

A simple web app connected to some LEDs which is intended for use as a demo during my entry for the IET [PresentIn10](https://www.theiet.org/involved/young-professionals/iet-presentin10-competition) competition.

# Setup 

Get a Raspberry Pi, some resistors, LEDs, jumper wires.

Connect appropriately.

Open a terminal.

```bash
pip3 install flask gpiozero
export FLASK_APP = web_blink.py
python3 -m flask run
# If you want other people to be able to access the demo, use:
python3 -m flask run --host 0.0.0.0
```

