#checking contents of db
from market import app, db
from market.models import User, Item

with app.app_context():

    print("\n--- ALL USERS ---")
    users = User.query.all()

    for user in users:
        print(
            f"ID: {user.id}, "
            f"Username: {user.username}, ",
            f"Password: {user.password_hash}",
            f"Email: {user.email_address}, "
            f"Budget: {user.budget}"
        )

    print("\n--- ALL ITEMS ---")
    items = Item.query.all()

    for item in items:
        owner = User.query.get(item.owner)

        print(
            f"ID: {item.id}, "
            f"Name: {item.name}, "
            f"Price: {item.price}, "
            f"Owner: {owner.username if owner else 'None'}"
        )