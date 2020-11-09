"""CRUD operations."""

from model import db, Product, connect_to_db

import datetime


def create_product(channel_name,product_description, option, product_url, price, added_on, number_sold, margin, updated_on):
   

    product = Product(channel_name=channel_name,
                  product_description=product_description,
                  option=option,
                  product_url=product_url,
                  price=price,
                  added_on=added_on,
                  number_sold=number_sold,
                  margin=margin,
                  updated_on=updated_on)

    db.session.add(product)

    db.session.commit()

    return product

def get_products():
    """Return all rows of product data."""

    return Product.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
