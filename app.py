from flask import Flask, render_template, url_for, request, send_file, redirect
import json
import csv
import math

app = Flask(__name__) #Object Declare
deny = "Request Denied! Please do not hack this web :'("


@app.route('/') #Home Page atau Halaman Menu
def index():
    return  render_template('index.html')

@app.route('/akar', methods = ['GET', 'POST']) #Halaman Kalkulator
def calcul():
    if request.method == "GET":
        return render_template('kalku.html')
    elif request.method == "POST":
        number = int(request.form['angka'])
        hasil = math.sqrt(number)
        hasil = str(hasil)
        return pass

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

@app.route('/csvtojson') #Halaman form csv to tabel json
def csvtojson():
    return render_template('csvtojson.html')        # panggil html converter

@app.route('/convert', methods = ['GET', 'POST'])
def convert():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)

    data = {}
    with open(f.filename) as csvFile:                     # Buka file yang diupload
        csvReader = csv.DictReader(csvFile)
        for i, rows in enumerate(csvReader):
            id = i
            data[id] = rows

    with open('array.json', 'w') as jsonFile:       # Convert file tersebut jadi json
        jsonFile.write(json.dumps(data, indent=4))

    return send_file('array.json', as_attachment=True)      # Download JSON


if __name__ == "__main__":
    app.run(debug=True) #Run App dengan debug aktif

