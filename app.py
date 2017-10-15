from flask import Flask, render_template, flash, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"

if __main__ == __name__:
    app.run(debug=True)