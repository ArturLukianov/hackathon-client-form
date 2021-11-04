from flask import Flask, send_from_directory, redirect
from flask_cors import cross_origin


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/index.html')


@app.route('/<path:path>')
@cross_origin()
def send_file(path):
    response = send_from_directory("./public", path)
    return response
