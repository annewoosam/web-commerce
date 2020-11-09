"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb web_commerce')

os.system('createdb web_commerce')

model.connect_to_db(server.app)

model.db.create_all()


# Create product table's initial data.

with open('data/product.json') as f:

    product_data = json.loads(f.read())

product_in_db = []

for product in product_data:
    channel_name, product_description, option, product_url, price, added_on, number_sold, margin, updated_on= (
                                   product['channel_name'],
                                   product['product_description'],
                                   product['option'],
                                   product['product_url'],
                                   product['price'],
                                   product['added_on'],
                                   product['number_sold'],
                                   product['margin'],
                                   product['updated_on'])

    db_product = crud.create_product(
                                 channel_name,
                                 product_description,
                                 option,
                                 product_url,
                                 price,
                                 added_on,
                                 number_sold,
                                 margin,
                                 updated_on)

    product_in_db.append(db_product)
