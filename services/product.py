from models.product import Product
from sqlalchemy.orm import Session
from dto import product


def create_product(data: product.Product, db: Session):
    product = Product(title=data.title)
    try:
        db.add(product)
        db.commit()
        db.refresh(product)
    except Exception as a:
        print(a)

    return product


def get_product(id: int, db: Session):
    return db.query(Product).filter(Product.id == id).first()


def update_product(data: product.Product, db: Session, id: int):
    product = db.query(Product).filter(Product.id == id).first()
    product.title = data.title
    db.add(product)
    db.commit()
    db.refresh(product)


def remove_product(id: int, db: Session):
    product = db.query(Product).filter(Product.id == id).delete()
    db.commit()

    return product


