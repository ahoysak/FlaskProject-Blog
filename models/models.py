from app import db


class Employee(db.Model):
    name = db.Column(db.String(25))
    email = db.Column(db.String(25))
    department_type = db.Column(db.String(25))
    department_id = db.Column(db.Integer, primary_key=True)


class Plant(db.Model):
    location = db.Column(db.String(25))
    name_plant = db.Column(db.String(25))
    director_id = db.Column(db.Integer, primary_key=True)


class Salon(db.Model):
    name_salon = db.Column(db.String(25))
    adress_salon = db.Column(db.String(25))
    id_salon = db.Column(db.Integer, primary_key=True)