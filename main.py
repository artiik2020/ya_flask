import os

from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='static/templates')


@app.route('/<title>')
def index1(title):
    return render_template("base.html", title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.12')
