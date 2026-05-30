from market import app, db
from market.models import User, Item

with app.app_context():

    db.create_all()

    # Prevent reseeding every restart
    if User.query.first():
        print("Database already seeded.")
        exit()

    users = [

        User(
            username="kunal",
            email_address="kunal@gmail.com",
            password="pass1",
            budget=5000
        ),

        User(
            username="alex",
            email_address="alex@gmail.com",
            password="pass2",
            budget=3000
        ),

        User(
            username="bot",
            email_address="bot123@gmail.com",
            password="kaushik",
            budget=1000
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    items = [

        Item(
            name="iPhone",
            price=1000,
            barcode="111111111111",
            description="Apple smartphone",
            owner=1
        ),

        Item(
            name="Laptop",
            price=2000,
            barcode="222222222222",
            description="Gaming laptop",
            owner=1
        ),

        Item(
            name="Keyboard",
            price=150,
            barcode="333333333333",
            description="Mechanical keyboard",
            owner=2
        ),

        Item(
            name="PS5",
            price=700,
            barcode="444444444444",
            description="PlayStation 5",
            owner=None
        ),

        Item(
            name="Xbox",
            price=650,
            barcode="555555555555",
            description="Xbox Series X",
            owner=None
        )
    ]

    db.session.add_all(items)
    db.session.commit()

    print("Database initialized and seeded!")