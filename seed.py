from app import db, Category, Product

with app.app_context():
    db.create_all()

    if not Category.query.all():
        categories = [
            Category(name="Electronics"),
            Category(name="Clothing"),
            Category(name="Books")
        ]
        db.session.add_all(categories)
        db.session.commit()

    if not Product.query.all():
        products = [
            Product(name="Smartphone", description="Latest model", price=699.99, category_id=1),
            Product(name="T-Shirt", description="Cotton t-shirt", price=19.99, category_id=2),
            Product(name="Database Design Book", description="Learn SQL and modeling", price=49.99, category_id=3),
        ]
        db.session.add_all(products)
        db.session.commit()
