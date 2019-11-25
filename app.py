import os
from flask import Flask, render_template, redirect, request, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'darren_secret'

app.config["MONGO_DBNAME"] = 'msProject3'
app.config["MONGO_URI"] = 'mongodb+srv://darrenmcgill:darrenmcgill35@myfirstcluster-qtggr.mongodb.net/msProject3'

mongo = PyMongo(app)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("Thanks, You have subscribed")
    return render_template("index.html")


@app.route('/blog', methods=["GET", "POST"])
def blog():
    return render_template("blog.html", page_title="Blog")


@app.route('/add_a_player', methods=["GET", "POST"])
def add_a_player():
    return render_template("add_a_player.html", page_title="Add & Review", players=mongo.db.players.find())


@app.route('/insert_player', methods=['POST'])
def insert_player():
    reviews = mongo.db.reviews
    print("aa: " + str(request.form.to_dict))
    reviews.insert_one({
        'player_name': request.form.get('player_name'),
        'player_club': request.form.get('player_club'),
        'player_position': request.form.get('player_position'),
        'player_review': request.form.get('player_review'),
        'issue_date': request.form.get('picker'),
        'review_from': request.form.get('review_from')
    })
    return redirect(url_for('review_a_player'))


@app.route('/review_a_player', methods=["GET", "POST"])
def review_a_player():
    return render_template("review_a_player.html", page_title="Edit & Delete", reviews=mongo.db.reviews.find())


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editreview.html', review=the_review,
                           categories=all_categories)


@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
    reviews = mongo.db.tasks
    reviews.update({'_id': ObjectId(review_id)},
    {
        'player_name': request.form.get('player_name'),
        'player_club': request.form.get('player_club'),
        'player_position': request.form.get('player_position'),
        'player_review': request.form.get('player_review'),
        'issue_date': request.form.get('picker'),
        'review_from': request.form.get('review_from')
    })
    return redirect(url_for('get_reviews'))


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    return redirect(url_for('review_a_player'))


@app.route('/merchandise', methods=["GET", "POST"])
def merchandise():
    return render_template("merchandise.html", page_title="Merchandise")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
