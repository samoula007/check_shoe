from flask import Flask
from threading import Thread

# easy template to keep the server alive
app = Flask('')


@app.route('/')
def home():
    return "Checking wanting shoe size availability..."


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
