from flask import Flask, render_template
import requests as re

app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if re.method == "POST":
        return
    else:
        return

if __name__ == "__main__":
    app.run(debug=True)
