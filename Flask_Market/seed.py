#initialising the database
#ran this before register

from market import app, db
from market.models import User, Item

with app.app_context():

    # Optional: clear old data
    db.drop_all()
    db.create_all()

    # Users
    user1 = User(
        username="kunal",
        email_address="kunal@gmail.com",
        password_hash="pass1",
        budget=5000
    )

    user2 = User(
        username="alex",
        email_address="alex@gmail.com",
        password_hash="pass2",
        budget=3000
    )

    db.session.add_all([user1, user2])
    db.session.commit()

    # Items
    item1 = Item(
        name="iPhone",
        price=1000,
        barcode="111111111111",
        description="Apple smartphone",
        owner=user1.id
    )

    item2 = Item(
        name="Laptop",
        price=2000,
        barcode="222222222222",
        description="Gaming laptop",
        owner=user1.id
    )

    item3 = Item(
        name="Keyboard",
        price=150,
        barcode="333333333333",
        description="Mechanical keyboard",
        owner=user2.id
    )

    db.session.add_all([item1, item2, item3])
    db.session.commit()

    print("Database seeded successfully!")