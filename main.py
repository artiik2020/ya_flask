from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates')


@app.route('/distribution')
def index1():
    return render_template("add_to_base.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.12')
