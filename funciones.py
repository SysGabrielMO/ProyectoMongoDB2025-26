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

#MODIFICACION
def actualizar_uno(code, nueva_valoracion):
    resultado = coleccion.update_one(
        {"code": code},
        {"$set": {"valoracion": nueva_valoracion, "ultima_inspeccion": datetime.now()}}
    )
    return resultado.modified_count

def actualizar_varios(country):
    resultado = coleccion.update_many(
        {"country": country},
        {"$set": {"revision_pendiente": True}}
    )
    return resultado.modified_count

def reemplazar_uno(code, name, notas):
    resultado = coleccion.replace_one(
        {"code": code},
        {
            "code": code,
            "name": name,
            "notas": notas,
            "ultima_inspeccion": datetime.now(),
            "activo": True
        }
    )
    return resultado.modified_count

#CONSULTAS SIMPLES 
def consulta_por_pais(country):
    return list(coleccion.find(
        {"country": country},
        {"_id": 0, "code": 1, "name": 1, "city": 1, "valoracion": 1, "pasajeros_anuales": 1}
    ).sort("valoracion", -1))


def consulta_mejor_valorados(limite):
    return list(coleccion.find(
        {"activo": True},
        {"_id": 0, "code": 1, "name": 1, "country": 1, "valoracion": 1}
    ).sort("valoracion", -1).limit(limite))