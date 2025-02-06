from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index() -> str:
    return "<h1>Página de inicio.</h1>"

@app.route("/hello")
def hello() -> str:
    return "<h1>Hola mundo.</h1>"
