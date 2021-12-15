from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/adityajoshi/PycharmProjects/cafe-website/cafes.db'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


class Cafe(db.Model):
    __table__ =  db.Model.metadata.tables['cafe']

    def __repr__(self):
        return '<Cafe %r>' % self.name

#
# class Cafes(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(500), unique=True, nullable=False)
#     map_url = db.Column(db.String(500), unique=True, nullable=False)
#     img_url = db.Column(db.String(500), unique=True, nullable=False)
#     location = db.Column(db.String(500), unique=True, nullable=False)
#     has_sockets = db.Column(db.Integer, nullable=False)
#     has_toilet = db.Column(db.Integer, nullable=False)
#     has_wifi = db.Column(db.Integer, nullable=False)
#     can_take_calls = db.Column(db.Integer, nullable=False)
#     seats = db.Column(db.String(100), nullable=False)
#     coffee_price = db.Column(db.String(100), nullable=False)
#
#     def __repr__(self):
#         return '<Cafe %r>' % self.name

# db.create_all()

@app.route('/')
def home():  # put application's code here
    cafe_list = Cafe.query.all()
    print(cafe_list)
    return render_template('index.html', cafe_list=cafe_list)


@app.route('/details/<int:id>')
def cafe_details(id):
    cafe_detail = Cafe.query.get(id)
    print(cafe_detail.seats)
    return render_template('cafe_details.html', details=cafe_detail)


if __name__ == '__main__':
    app.run(debug=True)
