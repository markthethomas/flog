from flask import Flask, url_for

app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login(username):
    return username

@app.route('/<year>/<month>/<day>/<name>', methods=['GET'])
def fname(year, month, day, name):
    return year

if __name__ == '__main__':
    app.run()