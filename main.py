from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>HELLO WORLD!</H1>'
app.run()