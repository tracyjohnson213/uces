import os
import json
from flask import Flask, render_template  # Flask class

app = Flask(__name__)  # instance of Flask


@app.route('/')  # route decorator
def index():  # defined view
    return render_template('index.html')


@app.route('/services')
def services():
    data = []
    with open("data/services.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        'services.html', page_title='Services', services=data)


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact')


@app.route('/login')
def login():
    return render_template('login.html', page_title='Login')


if __name__ == '__main__':  # default module of python
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

# https://startbootstrap.com/previews/business-casual/
# https://www.ucesprotectionplan.com/default.aspx?rid=tjohnson224
# google images