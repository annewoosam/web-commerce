from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

# test = Product(channel_name='WinningCheckers', email_date='2020-01-31',number_subscribers = '1', month_end_at='2019-12-31', subscribers='0', views='1', minutes_watched='2', likes='3', comments='4', posts='5', shares='6')

class Product(db.Model):
    """A class for products."""
    
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    product_description = db.Column(db.String)

    option = db.Column(db.String)

    product_url = db.Column(db.String)

    price = db.Column(db.Integer)

    added_on = db.Column(db.Date)

    number_sold = db.Column(db.Integer)

    margin = db.Column(db.Integer)

    updated_on = db.Column(db.Date)

    def __repr__(self):
        return f'<Product product_id={self.product_id} channel_name={self.channel_name}>'

def connect_to_db(flask_app, db_uri='postgresql:///web_commerce', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)