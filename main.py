from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('flasky/index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('flasky/users.html', name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errorpages/404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errorpages/500.html'), 500