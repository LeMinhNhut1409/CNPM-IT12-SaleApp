from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from app import db


class Category(db.Model):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship("Product", backref="category", lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    from app import app

    with app.app_context():
        # c1 = Category(name="IPhone")
        # c2 = Category(name="IPad")
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(
            name="Iphone 15 128GB",
            price=20000000,
            image="https://cdn1.viettelstore.vn/Images/Product/ProductImage/1979390149.jpeg",
            category_id=1,
        )
        p2 = Product(
            name="Iphone 15 Pro 128GB",
            price=27990000,
            image="https://cdn.viettelstore.vn/Images/Product/ProductImage/1778159139.jpeg",
            category_id=1
        )
        p3 = Product(
            name="Iphone 15 Pro Max 256GB",
            price=27990000,
            image="https://cdn1.viettelstore.vn/Images/Product/ProductImage/1349547788.jpeg",
            category_id=1,
        )
        p4 = Product(
            name="Iphone 15 Plus 128GB",
            price=27990000,
            image="https://cdn1.viettelstore.vn/Images/Product/ProductImage/1877671236.jpeg",
            category_id=1,
        )
        p5 = Product(
            name="IPad Pro 11 (2022) WIFI 128GB",
            price=20090000,
            image="https://cdn1.viettelstore.vn/Images/Product/ProductImage/1668025194.jpeg",
            category_id=2,
        )
        p6 = Product(
            name="IPad Gen 10 WIFI 64GB",
            price=10890000,
            image="https://cdn1.viettelstore.vn/Images/Product/ProductImage/2145259476.jpeg",
            category_id=2,
        )

        db.session.add_all([p1, p2, p3, p4, p5, p6])
        db.session.commit()
        # db.create_all()
