import faker
from flask import Flask, render_template, request, redirect, url_for
from faker import Faker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from werkzeug.exceptions import HTTPException
import os

app = Flask(__name__)

faker = Faker(locale=["ru_RU", "es_ES"])


CONFIG_OBJ_PATH = f'config.{os.getenv("CONFIG", "DevelopmentConfig")}'

app.config.from_object(CONFIG_OBJ_PATH)

db = SQLAlchemy(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],
                       echo=True,
                       )


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    job = Column(String, nullable=False)
    company = Column(String(256))
    ssn = Column(String(256))
    residence = Column(String(256))
    blood_group = Column(String(256))
    username = Column(String(256), unique=True, nullable=False)
    name = Column(String(256), nullable=False)
    sex = Column(String(256), nullable=False)
    address = Column(String(256))
    mail = Column(String(256), unique=True)
    birthdate = Column(String(256))


db.metadata.create_all(engine)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        return redirect(url_for('new_user'))


@app.route("/about")
@app.route("/about/")
def about():
    pass
    return render_template("about.html")


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        new_user_data = faker.profile()
        new_user_data.pop("current_location")
        new_user_data.pop("website")
        new_user_data.pop("blood_group")
        return render_template('new_user.html', new_user_data=new_user_data)
    elif request.method == 'POST':
        user = User(
            job=request.form['job'],
            sex=request.form['sex'],
            ssn=request.form['ssn'],
            name=request.form['name'],
            company=request.form['company'],
            mail=request.form['mail'],
            address=request.form['address'],
            birthdate=request.form['birthdate'],
            residence=request.form['residence'],
            username=request.form['username'],
        )
        db.session.begin()
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users'))


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = db.session.query(User).all()

        return render_template('users.html', users=users)
    elif request.method == 'POST':

        return render_template('users.html')


@app.errorhandler(HTTPException)
def error_handler(error):
    print(error)
    return render_template('404.html')


@app.errorhandler(Exception)
def error_handler_b(error):
    print(error)
    return render_template('404.html')


if __name__ == "__main__":
    app.debug = True
    app.register_error_handler(404, error_handler)
    app.register_error_handler(500, error_handler_b)
    app.run(host='0.0.0.0')


