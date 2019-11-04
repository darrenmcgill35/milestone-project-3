import os
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'darren_secret'


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("Thanks, You have subscribed")
    return render_template("index.html")


@app.route('/review',methods=["GET", "POST"])
def review():
    return render_template("review.html", page_title="Reviews")


@app.route('/add_a_player',methods=["GET", "POST"])
def add_a_player():
    return render_template("add_a_player.html", page_title="Add a Player")


@app.route('/review_a_player',methods=["GET", "POST"])
def review_a_player():
    return render_template("review_a_player.html", page_title="Review a Player")


@app.route('/merchandise',methods=["GET", "POST"])
def merchandise():
    return render_template("merchandise.html", page_title="Merchandise")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
