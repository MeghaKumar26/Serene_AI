from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = 'your_secret_key'
socketio = SocketIO(app)

# Simple user storage (in-memory for demonstration purposes)
users = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Allow any username and password
    if username and password:
        session['username'] = username
        users[username] = password  # Store user credentials
        return redirect(url_for('chat'))

    return redirect(url_for('index'))

@app.route('/chat')
def chat():
    if 'username' in session:
        return render_template('chat.html', username=session['username'])
    return redirect(url_for('index'))

@socketio.on('send_message')
def handle_send_message(data):
    emit('receive_message', {'username': session['username'], 'message': data['message']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
