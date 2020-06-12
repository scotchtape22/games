from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/login')
def hello_world():
    return 'Hello, World!'

@app.route('/leagues')
def hello_world():
    return 'Hello, World!'
    
@app.route('/teams')
def hello_world():
    return 'Hello, World!'

@app.route('/games')
def hello_world():
    return 'Hello, World!'

@app.route('/forum')
def hello_world():
    return 'Hello, World!'
