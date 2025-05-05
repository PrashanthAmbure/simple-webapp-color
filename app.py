import os
from flask import Flask
from flask import render_template
import socket
import random
import signal

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "orange": "#ff8000",
    "pink": "#be2edd",
    "yellow": "#ffff00"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","orange","pink","yellow"])

@app.route("/")
def main():
    #return "Hello"
    print(color)
    return render_template('welcome.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('welcome.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/read_file')
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return render_template('welcome.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server shutting down...'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
