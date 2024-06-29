from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config.from_pyfile("config.py")

from models import db,sucursal,repartidor,paquete,transporte

@app.route("/")
def inicio():
    return render_template("inicio.html",sucursales=sucursal.query.all())
@app.route("/xsucursal/<int:id>",methods=['GET'])
def xsucursal(id):
    sucursal_actual=sucursal.query.get(id)
    session['id_sucur']=sucursal_actual.id
    return render_template("menu_despachantes.html")
@app.route("/xsucusal/resgistrar_paquete",methods=['GET','POST'])
def registrar_paquete():
    if request.method=='POST':
        if not request.form["peso"] or not request.form["nombre_destinatario"] or not request.form["direccion_destinatario"]:
            return render_template("error.html",error="el formulario no fue completado")
        else:
            xpeso=request.form.get("peso")
            xnom=request.form.get("nombre_destinatario")
            xdir=request.form.get("direccion_destinatario")
            ultimo_paquete = paquete.query.order_by(paquete.id.desc()).first()
            xnum=ultimo_paquete.numeroenvio+20
            xpaquete = paquete(numeroenvio=xnum, peso=xpeso, nomdestinatario=xnom, dirdestinatario=xdir, entregado=False, observaciones='', idsucursal=int(session["id_sucur"]), idtransporte=0, idrepartidor=0)
            db.session.add(xpaquete)
            db.session.commit()
            return render_template("registrado_exitosamente.html")
    else:
        return render_template("registrar_paquetes.html",sucur=sucursal.query.get(int(session["id_sucur"])))
@app.route('/SeleccionSalidas', methods=['GET'])
def seleccion_salidas():
    return render_template('seleccionar_destino.html', sucursales=sucursal.query.all())
@app.route("/salida_transporte/<int:id>",methods=['GET','POST'])
def salida_transporte(id):
    sucursal_destino=sucursal.query.get(id)
    session["sucursal_destino"]=sucursal_destino.id
    paquetes = paquete.query.filter(paquete.entregado ==False, paquete.idrepartidor == 0).all()
    if request.method=='POST':
        try:
            xpaquetes=request.form.getlist('xpaquetes')
            assert xpaquetes!=None,"no selecciono una opcion"
            ultimo_transporte = transporte.query.order_by(transporte.id.desc()).first()
            xnum=ultimo_transporte.id+1
            fecha=str(datetime.now())
            xtransporte=transporte(numerotransporte=xnum, fechahorasalida=fecha, idsucursal=session['sucursal_destino'])
            for xid in xpaquetes:
                xpaquete=paquete.query.get(xid)
                xpaquete.idtransporte=xtransporte.id
            db.session.add(xtransporte)
            db.session.commit()
            return render_template("registrado_exitosamente.html")
        except AssertionError:
            return render_template("error.html",error="necesita seleccionar una opcion")
        except KeyError:
            return render_template("error.html",error="necesita seleccionar una opcion")
    else:
        return render_template("salida_transporte.html",paquetes=paquetes,id=sucursal_destino.id)
@app.route("/llegada_transporte", methods=['GET','POST'])
def llegada_transporte():
    id_suc=session["id_sucur"]
    xtransportes = transporte.query.filter(transporte.idsucursal == id_suc, transporte.fechahorallegada == None).all()
    if request.method=='POST':
        try:
            if not request.form["transportes"]:
                return render_template("error.html",error="no se selecciono ningun paquete")
            transportes_selec = request.form.getlist('transportes')
            for xid in transportes_selec:
                un_transporte=transporte.query.get(xid)
            if un_transporte:
                un_transporte.fechahorallegada=datetime.now()
                db.session.commit()
            return render_template("registrado_exitosamente.html")
        except KeyError:
            return render_template("error.html",error="necesita seleccionar una opcion")  
    else:
        return render_template("llegada_transporte.html",xtransportes=xtransportes)
if __name__=="__main__":
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.run(debug=True)