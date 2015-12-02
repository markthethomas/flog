from flask import Flask, url_for, render_template

app = Flask(__name__)

app.debug = True


@app.route('/', methods=['GET'])
def index():
    return 'Home!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login!'


@app.route('/<year>/<month>/<day>/<name>', methods=['GET'])
def fname(year, month, day, name):
    return render_template('layout.html', year=year, month=month, day=day, name=name)

if __name__ == '__main__':
    app.run()
