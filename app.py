from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from models import db, connect_db, Cupcakes
from forms import AddCupCake
app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

with app.app_context():
    
    db.create_all()

@app.route("/home")
def home():
    return redirect('cakes.html')

@app.route('/cupcakes')
def get_all_cupcakes_view():
    cakes = Cupcakes.query.all()
    form = AddCupCake()
    return render_template('cakes.html', cakes=cakes, form=form)

@app.route('/api/cupcakes')
def get_all_cupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcakes.query.all()]
    cupcakes = jsonify(cupcakes=cupcakes)
    return cupcakes

@app.route('/api/cupcakes/<int:id>')
def get_a_cupcake(id):
    cupcake = Cupcakes.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def post_a_cupcake():
    cupcake = Cupcakes(
        flavor = request.json["flavor"],
        size = request.json['size'],
        rating = request.json['rating'],
        image = request.json['image']
    )
    db.session.add(cupcake)
    db.session.commit()
    return(jsonify(cupcake=cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_a_cupcake(id):
    cupcake = Cupcakes.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor')
    cupcake.size = request.json.get('size')
    cupcake.rating = request.json['rating']
    cupcake.image = request.json['image']
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    todo = Cupcakes.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify(message="deleted")