from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask (__name__)
app.secret_key = "penjadwalan"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB'] = 'penjadwalan_kuliah'
app.config['MYSQL_CUMSORCLASS'] = 'DictCursor'

@app.route('/')
def home ():
    return template("login.html")
if __name__ == "__main__":
    app.run()

