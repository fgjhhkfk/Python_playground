# import os
# from flask import Flask, render_template, request, url_for, redirect, flash
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from forms import RezeptForm

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
