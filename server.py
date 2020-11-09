"""Server for YourFolder app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Product, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_products():

    stats=crud.get_products()
    
    product_id=[q[0] for q in db.session.query(Product.product_id).all()]

    channel_name=[q[0] for q in db.session.query(Product.channel_name).all()]
     
    product_description=[q[0] for q in db.session.query(Product.product_description).all()]
      
    option=[q[0] for q in db.session.query(Product.option).all()]

    product_url=[q[0] for q in db.session.query(Product.product_url).all()]

    price=[q[0] for q in db.session.query(Product.price).all()]

    added_on=[q[0] for q in db.session.query(Product.added_on).all()]

    number_sold=[q[0] for q in db.session.query(Product.number_sold).all()]

    margin=[q[0] for q in db.session.query(Product.margin).all()]

    updated_on=[q[0] for q in db.session.query(Product.updated_on).all()]
    
    # repeat through all columns needed

    return render_template('products.html', product_id=product_id, channel_name=channel_name, product_description=product_description, option=option, product_url=product_url, price=price, added_on=added_on, number_sold=number_sold, margin=margin, updated_on=updated_on)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()