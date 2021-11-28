from threading import local

from flask import Flask, render_template
from faker import Faker, providers
import collections


app = Flask(import_name=__name__)
faker_ru = Faker(locale="ru_RU")


@app.route("/")
@app.route("/index")
def index():
    index_data_fields = ["name", "address", "residence", "mail", "ssn", "job", "company"]
    index_data = collections.namedtuple("index_data", index_data_fields)
    fake_profile = faker_ru.profile()
    index_data.name = fake_profile['name']
    index_data.company = fake_profile['company']
    return render_template("index.html", index_data=index_data)


@app.route("/about")
@app.route("/about/")
def about():
    about_fields = ["head", "text", "footer"]
    about_data = collections.namedtuple("about", about_fields)
    about_data.company = faker_ru.company()
    about_data.text = faker_ru.sentence(nb_words=10)
    about_data.footer = faker_ru.name()

    return render_template("about.html", about=about_data)


if __name__ == "__main__":
    app.run()


