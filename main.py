#import logging
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mjk')
def hello_mjk():
    return 'Hello MJKOOL!'

# if __name__ == '__main__':
#     app.run()
