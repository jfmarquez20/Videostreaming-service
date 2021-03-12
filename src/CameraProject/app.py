from flask import Flask, render_template, Response
from image_gen import gen, name
from dropbox_api import send
import time
import dropbox
from dropbox.files import WriteMode
import os
from glob import iglob
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/streaming')
def streaming():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)

record = name()
send(record)


