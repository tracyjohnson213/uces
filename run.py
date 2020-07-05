import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)  # instance of Flask
app.secret_key = "some_secret"


# route and view for home page
@app.route('/')
def index():
    return render_template('index.html')


# route and view for services page
@app.route('/services')
def services():
    data = []
    with open("data/services.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        'services.html', page_title='Services', services=data)


# route and view for specific service
@app.route('/services/<service_name>')
def about_service(service_name):
    service = {}
    with open("data/services.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == service_name:
                service = obj
    return render_template('service.html', service=service)


# route and view for contact page
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".
              format(request.form["name"]))
    return render_template('contact.html', page_title='Contact')


# route and view for login page
@app.route('/login')
def login():
    return render_template('login.html', page_title='Login')


# default module of python
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

# https://startbootstrap.com/previews/business-casual/
# https://www.ucesprotectionplan.com/default.aspx?rid=tjohnson224
# google images
