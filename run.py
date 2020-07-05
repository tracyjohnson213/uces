import os
import json
from flask import Flask, render_template  # Flask class

app = Flask(__name__)  # instance of Flask


@app.route('/')  # route and view for home page
def index():
    return render_template('index.html')


@app.route('/services')  # route and view for services page
def services():
    data = []
    with open("data/services.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        'services.html', page_title='Services', services=data)


@app.route('/services/<service_name>')  # route and view for specific service
def about_service(service_name):
    service = {}
    with open("data/services.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == service_name:
                service = obj
    return render_template('service.html', service=service)


@app.route('/contact')  # route and view for contact page
def contact():
    return render_template('contact.html', page_title='Contact')


@app.route('/login')  # route and view for login page
def login():
    return render_template('login.html', page_title='Login')


if __name__ == '__main__':  # default module of python
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

# https://startbootstrap.com/previews/business-casual/
# https://www.ucesprotectionplan.com/default.aspx?rid=tjohnson224
# google images
