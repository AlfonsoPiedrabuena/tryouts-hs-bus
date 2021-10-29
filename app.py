from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    title = 'HS TryOut'
    return render_template('index.html', title=title)

@app.route('/us')
def us():
    title = 'Us'
    return render_template('us.html', title=title)

@app.route('/theme')
def theme():
    title='Theme'
    return render_template('theme.html', title=title)
    


#return render_template('index.html', title=title)