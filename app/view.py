from flask import render_template

from app import app
from models import Post



@app.route('/')
def index():

    return render_template('index.html')
