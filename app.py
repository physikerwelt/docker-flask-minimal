# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
