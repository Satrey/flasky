from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, URL


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
    form.name.data = ''
    return render_template('flasky/index.html', current_time=datetime.utcnow(), form=form, name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('flasky/users.html', name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errorpages/404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errorpages/500.html'), 500


class UserForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    mail = EmailField('E-mail')
    submit = SubmitField('Отправить')

