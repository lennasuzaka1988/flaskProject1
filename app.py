import datetime
import smtplib

from flask import Flask, render_template
from forms import ContactForm
from titlecase import titlecase
from datetime import date
import json
import random
import requests

blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
blogs = requests.get(blog_url).json()
url = "https://opencritic-api.p.rapidapi.com/game/reviewed-this-week"

headers = {
    "X-RapidAPI-Key": "f4d862d32amshd2fc2ad94eb9098p1dcce3jsnbbe43b9ee5ff",
    "X-RapidAPI-Host": "opencritic-api.p.rapidapi.com"
}

app = Flask(__name__)
app.secret_key = 'JSFL23847JFDKLFMSjdfjkaioFWEReaf'


@app.route('/')
def home_page():
    current_date = date.today()
    current_year = current_date.year
    return render_template('index.html', year=current_year)

# @app.route('/about')
# def about_page():

# @app.route('/store')
# def store_page():


@app.route('/blog')
def blog():
    post_objects = [i for i in blogs]
    current_date = date.today()
    current_year = current_date.year
    return render_template("blog.html", current_date=current_date, year=current_year, post=post_objects)

# @app.route('/open_critic_project')
# def open_critic_api():
#     response = requests.get(url, headers=headers).json()
#     game_name_img_score = []
#     for entry in response:
#         game_name_img_score.append((entry["name"], int(round(entry["topCriticScore"])),
#                                     "https://img.opencritic.com/" + entry['images']['box']['og']))
#     return render_template('opencritic_api_project.html', titles=game_name_img_score)

# @app.route('/contact')
# def contact_page():


@app.route('/blog/<int:num>')
def blog_page(num):
    year = date.today().year
    month = date.today().month
    datetime_object = datetime.datetime.strptime(str(month), "%m")
    month_name = datetime_object.strftime("%B")
    post = [i for i in blogs if i['id'] == num]
    return render_template('blog_page.html', post=post[0], year=year, month=month_name)


@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        email = contact_form.email.data
        message = contact_form.message.data
        to_addr = 'halfnhalflg@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.sendmail(from_addr=email, to_addrs=to_addr, msg=message)
        server.quit()
        return render_template('form_submit.html', form=contact_form)
    else:
        print("Invalid Credentials")

    return render_template('contact.html', form=contact_form)


if __name__ == '__main__':
    app.run(debug=True)

