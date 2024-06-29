from __main__ import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class sucursal(db.Model):
    __tablename__="sucursal"
    id=db.Column(db.Integer,primary_key=True)
    numero=db.Column(db.Integer,nullable=False,unique=True)
    provincia=db.Column(db.String,nullable=False)
    localidad=db.Column(db.String,nullable=False)
    direccion=db.Column(db.String,nullable=False)
    paquete=db.relationship("paquete", backref="sucursal")
    repartidor=db.relationship("repartidor", backref="sucursal")
    transporte=db.relationship("transporte", backref="sucursal")
class transporte(db.Model):
    __tablename__="transporte"
    id=db.Column(db.Integer,primary_key=True)
    numerotransporte=db.Column(db.Integer,nullable=False,unique=True)
    fechahorasalida=db.Column(db.String)
    fechahorallegada=db.Column(db.String)
    idsucursal=db.Column(db.Integer,db.ForeignKey("sucursal.id"))
    paquete=db.relationship("paquete",backref="transporte")
class repartidor(db.Model):
    __tablename__="repartidor"
    id=db.Column(db.Integer,primary_key=True)
    numero=db.Column(db.Integer,nullable=False,unique=True)
    nombre=db.Column(db.String,nullable=False,unique=True)
    dni=db.Column(db.Integer,nullable=False,unique=True)
    idsucursal=db.Column(db.Integer,db.ForeignKey("sucursal.id"))
    paquete=db.relationship("paquete", backref="repartidor")
class paquete(db.Model):
    __tablename__="paquete"
    id=db.Column(db.Integer,primary_key=True)
    numeroenvio=db.Column(db.Integer,nullable=False,unique=True)
    peso=db.Column(db.Integer,nullable=False)
    nomdestinatario=db.Column(db.String,nullable=False)
    dirdestinatario=db.Column(db.String,nullable=False)
    entregado=db.Column(db.Boolean,nullable=False)
    observaciones=db.Column(db.String)
    idsucursal=db.Column(db.Integer,db.ForeignKey("sucursal.id"))
    idtransporte=db.Column(db.Integer,db.ForeignKey("transporte.id"))
    idrepartidor=db.Column(db.Integer,db.ForeignKey("repartidor.id"))