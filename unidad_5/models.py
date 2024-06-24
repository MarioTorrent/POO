from __main__ import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
class sucursal(db.Model):
    __tablename__="sucursal"
    id=db.column(db.Integer,primary_key=True)
    numero=db.column(db.Integer,nullable=False,unique=True)
    provincia=db.column(db.String,nullable=False)
    localidad=db.column(db.String,nullable=False)
    direccion=db.column(db.String,nullable=False)
class transporte(db.Model):
    __tablename__="transporte"
    id=db.column(db.Integer,primary_key=True)
    numerotransporte=db.column(db.Integer,nullable=False,unique=True)
    fechahorasalida=db.column(db.String)
    fechahorallegada=db.column(db.String)
    idsucursal=db.column(db.Integer,db.ForaignKey("sucursal.id"))
    paquete=db.relationship("paquete",backref="transporte")
class repartidor(db.Model):
    __tablename__="repartidor"
    id=db.column(db.Integer,primary_key=True)
    numero=db.column(db.Integer,nullable=False,unique=True)
    nombre=db.column(db.String,nullable=False,unique=True)
    dni=db.column(db.Integer,nullable=False,unique=True)
    idsucursal=db.column(db.Integer,db.ForaignKey("sucursal.id"))
class paquete(db.Model):
    __tablename__="paquete"
    id=db.column(db.Integer,primary_key=True)
    numeroenvio=db.column(db.Integer,nullable=False,unique=True)
    peso=db.column(db.Integer,nullable=False)
    nomdestinatario=db.column(db.String,nullable=False)
    dirdestinatario=db.column(db.String,nullable=False)
    entregado=db.column(db.Boolean,nullable=False)
    observaciones=db.column(db.String)
    idsucursal=db.column(db.Integer,db.ForeignKey("sucursal.id"))
    idtransporte=db.column(db.Integer,db.ForaignKey("transporte.id"))
    idrepartidor=db.column(db.Integer,db.ForaignKey("repartidor.id"))