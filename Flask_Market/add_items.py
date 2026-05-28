from market import app, db
from market.models import User, Item

with app.app_context():

    # Get users
    kunal = User.query.filter_by(username="kunal").first()
    alex = User.query.filter_by(username="alex").first()
    bot = User.query.filter_by(username="bot").first()
    kunal2 = User.query.filter_by(username="kunal2").first()

    items = [

        # Owned by kunal
        Item(
            name="MacBook",
            price=2500,
            barcode="444444444444",
            description="Apple laptop",
            owner=kunal.id
        ),

        Item(
            name="AirPods",
            price=300,
            barcode="555555555555",
            description="Wireless earbuds",
            owner=kunal.id
        ),

        # Owned by alex
        Item(
            name="Monitor",
            price=400,
            barcode="666666666666",
            description="27 inch monitor",
            owner=alex.id
        ),

        Item(
            name="Mouse",
            price=80,
            barcode="777777777777",
            description="Gaming mouse",
            owner=alex.id
        ),

        # Owned by bot
        Item(
            name="Tablet",
            price=600,
            barcode="888888888888",
            description="Android tablet",
            owner=bot.id
        ),

        Item(
            name="Speaker",
            price=200,
            barcode="999999999999",
            description="Bluetooth speaker",
            owner=bot.id
        ),

        # Owned by kunal2
        Item(
            name="Camera",
            price=1200,
            barcode="121212121212",
            description="DSLR Camera",
            owner=kunal2.id
        ),

        Item(
            name="Printer",
            price=350,
            barcode="343434343434",
            description="Color printer",
            owner=kunal2.id
        ),

        # Unowned items
        Item(
            name="PS5",
            price=700,
            barcode="565656565656",
            description="PlayStation 5",
            owner=None
        ),

        Item(
            name="Xbox",
            price=650,
            barcode="787878787878",
            description="Xbox Series X",
            owner=None
        ),

        Item(
            name="Smart Watch",
            price=250,
            barcode="909090909090",
            description="Fitness smartwatch",
            owner=None
        ),

        Item(
            name="Headphones",
            price=180,
            barcode="101010101010",
            description="Noise cancelling headphones",
            owner=None
        ),

        Item(
            name="Microphone",
            price=140,
            barcode="202020202020",
            description="USB microphone",
            owner=None
        ),

        Item(
            name="Desk Lamp",
            price=60,
            barcode="303030303030",
            description="LED desk lamp",
            owner=None
        ),

        Item(
            name="Router",
            price=110,
            barcode="404040404040",
            description="WiFi router",
            owner=None
        ),

        Item(
            name="SSD",
            price=220,
            barcode="505050505050",
            description="1TB SSD",
            owner=None
        ),

        Item(
            name="Graphics Card",
            price=1500,
            barcode="606060606060",
            description="RTX graphics card",
            owner=None
        ),

        Item(
            name="Webcam",
            price=90,
            barcode="707070707070",
            description="HD webcam",
            owner=None
        )
    ]

    db.session.add_all(items)
    db.session.commit()

    print("Items added successfully!")