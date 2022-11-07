from flask import Flask, render_template, url_for, request
import requests as re

app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/calculator', methods = ['GET', 'POST'])
def calcul():
    return render_template('kalku.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        Nama = request.form['nama']
        NIM = request.form['nim']
        return f"Nama anda adalah {Nama} dengan nim {NIM}"
    elif request.method == "GET":
        return render_template('upload.html')
    else:
        return 'HTTP methods error'

@app.route('/about', methods = ['GET', 'POST'])
def aboutme():
    return render_template('aboutme.html')

@app.route('/csvtojson', method = ['GET', 'POST'])
def csvtojson():
    return render_template('csvtojson.html')

if __name__ == "__main__":
    app.run(debug=True)
