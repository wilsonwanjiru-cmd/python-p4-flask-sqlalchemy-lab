from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.DateTime)

    animals = db.relationship('Animal', back_populates='zookeeper')

    def __repr__(self):
        return f'Zookeeper(id={self.id}, name={self.name},birthday={self.birthday},animals={self.animals})'


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean, unique=False, default=True)

    animals = db.relationship('Animal', back_populates='enclosure')

    def __repr__(self):
        return f'Enclosure(id={self.id}, environment={self.environment},open_to_visitors={self.open_to_visitors},animals={self.animals})'

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    zookeeper = db.relationship('Zookeeper', back_populates='animals')
    enclosure = db.relationship('Enclosure', back_populates='animals')

    def __repr__(self):

        return f'Animal(id={self.id}, name={self.name},species={self.species},zookeeper={self.zookeeper.name}, enclosure={self.enclosure.environment})'