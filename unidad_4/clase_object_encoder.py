from pathlib import Path
import json
from clase_gestor_jugadores import gestor_jugadores,jugador
class ObjectEncoder(object):
    def decodificador_diccionario(self,d):
        if "__class__" not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='gestor_jugadores':
                jugadores=d["jugadores"]
                djugador=jugadores[0]
                xgestor=class_()
                for i in range(len(jugadores)):
                    djugador=jugadores[i]
                    class_name=djugador.pop("__class__")
                    class_=eval(class_name)
                    atributos=djugador['__atributos__']
                    xjugador=class_(atributos["nombre"],atributos["puntos"],atributos["fecha"],atributos["hora"])
                    xgestor.agregar_jugador_json(xjugador)
            return xgestor
    def guardarJSONarchivo(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()
    def leerJSONarchivo(self,archi):
        with Path(archi).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario