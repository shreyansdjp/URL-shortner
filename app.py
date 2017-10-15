from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"

@app.route('/<string:name>')
def goto(name):
    return redirect("http://www.facebook.com", code=301)

if __name__ == '__main__':
    app.run(debug=True)