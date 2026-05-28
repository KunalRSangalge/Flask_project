from market import app, db
from market.models import User, Item

with app.app_context():

    # Drop old tables
    db.drop_all()

    # Create fresh tables
    db.create_all()

    # ---------------- USERS ----------------

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
        ),

        User(
            username="gasfs",
            email_address="gfsafas@gmail.com",
            password="kunaltg",
            budget=1000
        ),

        User(
            username="kunal2",
            email_address="kunal2@gmail.com",
            password="pass5",
            budget=1000
        ),

        User(
            username="kunal3",
            email_address="kunal3@gmail.com",
            password="pass6",
            budget=1000
        ),

        User(
            username="kunal4",
            email_address="kunal4@gmail.com",
            password="pass7",
            budget=1000
        ),

        User(
            username="kunal5",
            email_address="kunal5@gmail.com",
            password="pass8",
            budget=1000
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    # ---------------- ITEMS ----------------

    items = [

        # Owned items

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
            name="Monitor",
            price=400,
            barcode="444444444444",
            description="27 inch monitor",
            owner=2
        ),

        Item(
            name="Drone",
            price=900,
            barcode="555555555555",
            description="Camera drone",
            owner=4
        ),

        Item(
            name="VR Headset",
            price=500,
            barcode="666666666666",
            description="Virtual reality headset",
            owner=4
        ),

        Item(
            name="Smart TV",
            price=1300,
            barcode="777777777777",
            description="55 inch smart television",
            owner=5
        ),

        Item(
            name="Coffee Machine",
            price=250,
            barcode="888888888888",
            description="Automatic coffee maker",
            owner=5
        ),

        Item(
            name="Gaming Chair",
            price=450,
            barcode="999999999999",
            description="Ergonomic gaming chair",
            owner=6
        ),

        Item(
            name="Projector",
            price=750,
            barcode="121212121212",
            description="Full HD projector",
            owner=7
        ),

        Item(
            name="External HDD",
            price=160,
            barcode="131313131313",
            description="2TB external hard drive",
            owner=8
        ),

        # Market items (owner=None)

        Item(
            name="PS5",
            price=700,
            barcode="141414141414",
            description="PlayStation 5",
            owner=None
        ),

        Item(
            name="Xbox",
            price=650,
            barcode="151515151515",
            description="Xbox Series X",
            owner=None
        ),

        Item(
            name="Smart Watch",
            price=250,
            barcode="161616161616",
            description="Fitness smartwatch",
            owner=None
        ),

        Item(
            name="Headphones",
            price=180,
            barcode="171717171717",
            description="Noise cancelling headphones",
            owner=None
        ),

        Item(
            name="Microphone",
            price=140,
            barcode="181818181818",
            description="USB microphone",
            owner=None
        ),

        Item(
            name="Desk Lamp",
            price=60,
            barcode="191919191919",
            description="LED desk lamp",
            owner=None
        ),

        Item(
            name="Router",
            price=110,
            barcode="202020202020",
            description="WiFi router",
            owner=None
        ),

        Item(
            name="SSD",
            price=220,
            barcode="212121212121",
            description="1TB SSD",
            owner=None
        ),

        Item(
            name="Graphics Card",
            price=1500,
            barcode="232323232323",
            description="RTX graphics card",
            owner=None
        ),

        Item(
            name="Webcam",
            price=90,
            barcode="242424242424",
            description="HD webcam",
            owner=None
        )
    ]

    db.session.add_all(items)
    db.session.commit()

    print("Database seeded successfully!")