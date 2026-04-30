from pymongo import MongoClient
from datetime import datetime

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["aeropuertos_db"]
coleccion = db["aeropuertos"]


#INSERCIÓN 

def insertar_uno(code, name, city, country, lat, lon, activo, pasajeros, terminales, valoracion, notas, num_tiendas):
    doc = {
        "code": code,
        "name": name,
        "city": city,
        "country": country,
        "coordenadas": {"lat": lat, "lon": lon},
        "activo": activo,
        "pasajeros_anuales": pasajeros,
        "terminales": terminales,
        "inauguracion": datetime.now(),
        "ultima_inspeccion": datetime.now(),
        "valoracion": valoracion,
        "notas": notas if notas else None,
        "servicios": {
            "wifi": True,
            "parking": True,
            "hotel_cercano": False,
            "num_tiendas": num_tiendas
        }
    }
    resultado = coleccion.insert_one(doc)
    return resultado.inserted_id

def insertar_varios(lista_docs):
    resultado = coleccion.insert_many(lista_docs)
    return resultado.inserted_ids

#ELIMINACION 

def eliminar_uno(code):
    resultado = coleccion.delete_one({"code": code})
    return resultado.deleted_count

def eliminar_varios(country):
    resultado = coleccion.delete_many({"country": country})
    return resultado.deleted_count
