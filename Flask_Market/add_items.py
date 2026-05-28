from market import app, db
from market.models import User, Item

with app.app_context():
    

    items = [

        # Owned by user id 4
        Item(
            name="Drone",
            price=900,
            barcode="818181818181",
            description="Camera drone",
            owner=4
        ),

        Item(
            name="VR Headset",
            price=500,
            barcode="828282828282",
            description="Virtual reality headset",
            owner=4
        ),

        # Owned by user id 5
        Item(
            name="Smart TV",
            price=1300,
            barcode="838383838383",
            description="55 inch smart television",
            owner=5
        ),

        Item(
            name="Coffee Machine",
            price=250,
            barcode="848484848484",
            description="Automatic coffee maker",
            owner=5
        ),

        # Owned by user id 6
        Item(
            name="Gaming Chair",
            price=450,
            barcode="858585858585",
            description="Ergonomic gaming chair",
            owner=6
        ),

        Item(
            name="Mechanical Keyboard Pro",
            price=220,
            barcode="868686868686",
            description="RGB mechanical keyboard",
            owner=6
        ),

        # Owned by user id 7
        Item(
            name="Projector",
            price=750,
            barcode="878787878787",
            description="Full HD projector",
            owner=7
        ),

        Item(
            name="Electric Scooter",
            price=1800,
            barcode="888989898989",
            description="Battery powered scooter",
            owner=7
        ),

        # Owned by user id 8
        Item(
            name="External HDD",
            price=160,
            barcode="898989898989",
            description="2TB external hard drive",
            owner=8
        ),

        Item(
            name="Fitness Band",
            price=120,
            barcode="919191919191",
            description="Health tracking band",
            owner=8
        ),
    ]

    db.session.add_all(items)
    db.session.commit()

    print("Items added successfully!")