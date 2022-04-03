from flask import Flask

#create flask app instance
app = Flask(__name__)

#create flask routes
@app.route('/')
def hello_world():
    return 'Hello world'
