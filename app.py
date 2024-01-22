from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
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
def four():
    return render_template('4v4.html') 
@app.route('/custom')
def custom():
    return render_template('custom.html') 
if __name__ == '__main__':
    app.run(debug=True)