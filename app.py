from flask import Flask, render_template, url_for, request
import json

app = Flask(__name__) #Object Declare
deny = "Request Denied! Please do not hack this web :'("


@app.route('/') #Home Page atau Halaman Menu
def index():
    return  render_template('index.html')

@app.route('/calculator', methods = ['GET', 'POST']) #Halaman Kalkulator
def calcul():
    if request.method == "GET":
        return render_template('kalku.html')
    else:
        return deny

@app.route('/login', methods = ['GET', 'POST']) #Halaman form masukkan data
def login():
    if request.method == "POST":
        Nama = request.form['nama']
        NIM = request.form['nim']
        return f"Nama anda adalah {Nama} dengan nim {NIM}"
    elif request.method == "GET":
        return render_template('upload.html')
    else:
        return deny

@app.route('/about', methods = ['GET']) #Halaman biodata dan CV
def aboutme():
    if request.method == 'GET':
        return render_template('aboutme.html')
    else :
        return deny

@app.route('/csvtojson', methods = ['GET', 'POST']) #Halaman form csv to tabel json
def csvtojson():
    if request.method == 'GET':
        return render_template('csvtojson.html')
    elif request.method == "POST":
        return render_template('')
    else:
        return deny

if __name__ == "__main__":
    app.run(debug=True) #Run App dengan debug aktif
