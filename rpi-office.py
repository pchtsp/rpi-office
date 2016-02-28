from flask import Flask, render_template, jsonify
import time
# import RPi.GPIO as GPIO

num_pin = 17

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(num_pin, GPIO.OUT)
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/turn_light_on')
def turn_light_on():
    # GPIO.output(num_pin, True)
    data = "prueba de encendido"
    return jsonify(result=data)

@app.route('/turn_light_off')
def turn_light_off():
    # GPIO.output(num_pin, False)
    data = "prueba de apagado"
    return jsonify(result=data)

if __name__ == '__main__':
    app.run()
