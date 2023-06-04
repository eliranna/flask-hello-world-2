from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
  return 'Hello, World2!'


@app.route('/about')
def about():
  return 'About2'


app.run(host='0.0.0.0', port=81)
