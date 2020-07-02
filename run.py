import os
from flask import Flask, render_template  # Flask class

app = Flask(__name__)  # instance of Flask


@app.route('/')  # route decorator
def index():  # defined view
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':  # default module of python
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

# https://startbootstrap.com/previews/business-casual/
