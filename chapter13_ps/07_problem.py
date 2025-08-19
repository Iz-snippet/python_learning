#Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()