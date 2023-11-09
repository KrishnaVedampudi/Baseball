times_sent = 0
import random
from flask import Flask, render_template, request
from paho.mqtt import client as mqtt_client
import time

app = Flask(__name__)

@app.route('/')
def index():
    global detection
    client_run = connect()    
    client_run.loop_start()  
    time.sleep(1)
    status = int(detection)
    return render_template('index.html',)

broker = "broker.emqx.io"
port = 1883
topic = "1V1"

client_id = 'test'
username = 'emqx'
password = ''

detection = 1

def connect():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.on_message = on_message
    client.subscribe(topic)
    return client


def on_connect(client: mqtt_client, userdata, flags, rc):
    global times_sent
    print("Connected with result code " + str(rc))
    client.subscribe(topic)
    if times_sent==0:
       client.publish(topic, "Player joined")    
    times_sent = 1
    print("BOOH!")


# Define the lobby topic

# Track the number of players in the lobby
players_in_lobby = 0


def on_message(client, userdata, message):       
    client.publish("game_start")

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/signup')
def signup():
    return render_template('sign-up.html')
@app.route('/verification')
def verification():
    return render_template('otp-verification.html')
@app.route('/main')
def main():
    return render_template('main.html')
@app.route('/lobby')
def lobby():
    return render_template('lobby.html')
@app.route('/arena')
def arena():
    return render_template('arena.html')
@app.route('/singleplayer')
def singleplayer():
    return render_template('singleplayer.html')  

if __name__ == '__main__':
    app.run(debug=True)
