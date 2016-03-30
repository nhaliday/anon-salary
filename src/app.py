from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Index page"

@app.route('/hello/<username>')
def hello(username):
    return "Hello {}!".format(username)

@app.route('/add/<int:x>+<int:y>')
def add(x, y):
    return str(x + y)

if __name__ == '__main__':
    app.run(debug=True)