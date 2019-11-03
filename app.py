import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/review')
def review():
    return render_template("review.html")


@app.route('/add_a_player')
def add_a_player():
    return render_template("add_a_player.html")

@app.route('/review_a_player')
def review_a_player():
    return render_template("review_a_player.html")

@app.route('/merchandise')
def merchandise():
    return render_template("merchandise.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
