from flask import Flask 

application = Flask(__name__)

@application.route("/")
def main():
    return "<h1>Hello World from AWS EC2 via Docker</h1>"

@application.route("/hello")
def hello():
    return "<h1>Hello from '/hello' </h1>"
