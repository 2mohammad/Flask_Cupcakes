from models import db, Cupcakes
from app import app

db.init_app(app)


def run_seed():
    c1 = Cupcakes(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcakes(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )
    db.session.add_all([c1, c2])
    db.session.commit()

with app.app_context():
    run_seed()
