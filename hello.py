from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello() -> str:
    return "Hola mundo"
