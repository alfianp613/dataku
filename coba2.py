from flask import Flask, render_template, redirect, url_for, request
from flask import jsonify
import pandas as pd

app = Flask(__name__, template_folder='templates')

@app.route('/')
def coba():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)