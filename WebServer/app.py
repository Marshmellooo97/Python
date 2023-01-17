from flask import Flask, render_template
import time
import os
from re import I
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(7, 1)
GPIO.output(11,1)
GPIO.output(12,1)
GPIO.output(13,1)
GPIO.output(15,1)
GPIO.output(16,1)
GPIO.output(18,1)
GPIO.output(22,1)

app = Flask(__name__)

@app.route("/")
def home():
    def pumpen(pumpe, zeit):
        GPIO.output(pumpe, hi)
        time.sleep(zeit)
        GPIO.output(pumpe, lo)
        time.sleep(0.3)
        
    def sexOnTheBeach(größe, stärke):
        pumpen(pumpe1,2 * größe + stärke)
        pumpen(pumpe2,1 * größe)
        pumpen(pumpe3,3 * größe - (stärke/2))
        pumpen(pumpe4,3 * größe- (stärke/2))

    def cubraLibre(größe, stärke):
        stärke += 1
        pumpen(pumpe5,2 * größe + stärke)
        pumpen(pumpe6,4 * größe - stärke)

    hi = 0
    lo = 1
    pumpe1 = 7
    pumpe2 = 11
    pumpe3 = 12
    pumpe4 = 13
    pumpe5 = 15
    pumpe6 = 16
    pumpe7 = 18
    pumpe8 = 22

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pumpe1, GPIO.OUT)
    GPIO.setup(pumpe2, GPIO.OUT)
    GPIO.setup(pumpe3, GPIO.OUT)
    GPIO.setup(pumpe4, GPIO.OUT)
    GPIO.setup(pumpe5, GPIO.OUT)
    GPIO.setup(pumpe6, GPIO.OUT)
    GPIO.setup(pumpe7, GPIO.OUT)
    GPIO.setup(pumpe8, GPIO.OUT)
    
    
    
    return render_template("home.html")

@app.route("/a")
def einstellung():
    return render_template("einstellung.html")
    
    
    
if __name__ == "__main__":
    app.run(debug=True)