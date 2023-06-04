from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
  return 'Hello, World2!'


@app.route('/api/about')
def about():
  return jsonify({'text': 'reply'})


#app.run(host='0.0.0.0', port=81)
