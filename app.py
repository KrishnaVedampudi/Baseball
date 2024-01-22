
from flask import Flask, render_template, request

times_sent = 0
import random
from flask import Flask, render_template, request
from paho.mqtt import client as mqtt_client
import time


app = Flask(__name__)
@app.route('/')
def index():

    return render_template('index.html')

    return render_template('index.html',)
mode = ""
broker = "broker.emqx.io"
port = 1883
topic = "1V1"

client_id = 'test'
username = 'emqx'
password = ''
detection = 1

players_in_lobby = 0

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
    global players_in_lobby        
    if times_sent==0:
       client.publish(topic, "Player joined")  
       print("BOOH!")  
    times_sent = 1

def on_message(client, userdata, message):
    global players_in_lobby
    print("Got it bro")  
    message = message.payload.decode('utf-8')    
    print(message)
    if message == "Player joined": 
        players_in_lobby = players_in_lobby+1
        client.publish(topic, "game_start")
        print(players_in_lobby)
        one()
    if message == "Player left":
        players_in_lobby = players_in_lobby-1
    if message == "game_start":
        one()    
    

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

def lobby():
    global detection
    client_run = connect()    
    client_run.loop_start()  
    time.sleep(1)
    status = int(detection)

    return render_template('lobby.html')
@app.route('/arena')
def arena():
    return render_template('arena.html')
@app.route('/singleplayer')
def singleplayer():
    return render_template('singleplayer.html') 

@app.route('/one')
def one():
    return render_template('1v1.html')   
@app.route('/two')
def two():
    return render_template('2v2.html') 
@app.route('/three')
def three():
    return render_template('3v3.html') 
@app.route('/four')

@app.route('/1v1')
def one():
    return render_template('1v1.html')   
@app.route('/2v2')
def two():
    return render_template('2v2.html') 
@app.route('/3v3')
def three():
    return render_template('3v3.html') 
@app.route('/4v4')

def four():
    return render_template('4v4.html') 
@app.route('/custom')
def custom():
    return render_template('custom.html') 

if __name__ == '__main__':
    app.run(debug=True)
