from funciones import (
    insertar_uno, insertar_varios,
    eliminar_uno, eliminar_varios,
    actualizar_uno, actualizar_varios, reemplazar_uno,
    consulta_por_pais, consulta_mejor_valorados,
    consulta_por_terminal, consulta_num_terminales,
    consulta_por_tiendas, consulta_sin_hotel,
    consulta_agrupacion_por_pais
)


#PANTALLAS DE MENU

MENU_PRINCIPAL = """
╔══════════════════════════════════════╗
║       GESTION DE AEROPUERTOS        ║
╠══════════════════════════════════════╣
║  1. Insertar                        ║
║  2. Eliminar                        ║
║  3. Modificar                       ║
║  4. Consultas simples               ║
║  5. Consultas con arrays            ║
║  6. Consultas con doc. embebido     ║
║  7. Consulta de agrupacion          ║
║  0. Salir                           ║
╚══════════════════════════════════════╝
"""

MENU_INSERTAR = """
--- INSERTAR ---
1. Insertar un aeropuerto (insertOne)
2. Insertar varios aeropuertos (insertMany)
0. Volver
"""

MENU_ELIMINAR = """
--- ELIMINAR ---
1. Eliminar por codigo IATA (deleteOne)
2. Eliminar todos los de un pais (deleteMany)
0. Volver
"""

MENU_MODIFICAR = """
--- MODIFICAR ---
1. Cambiar valoracion (updateOne)
2. Marcar revision pendiente por pais (updateMany)
3. Reemplazar aeropuerto completo (replaceOne)
0. Volver
"""

MENU_CONSULTAS_SIMPLES = """
--- CONSULTAS SIMPLES ---
1. Buscar por pais
2. Ver los N mejor valorados
0. Volver
"""

MENU_CONSULTAS_ARRAY = """
--- CONSULTAS CON ARRAYS ---
1. Buscar por terminal
2. Buscar por numero exacto de terminales
0. Volver
"""

MENU_CONSULTAS_EMBEBIDO = """
--- CONSULTAS CON DOC. EMBEBIDO ---
1. Aeropuertos con mas tiendas que N
2. Aeropuertos sin hotel cercano
0. Volver
"""


# ─── ACCIONES ─────────────────────────────────────────────────

def accion_insertar():
    print(MENU_INSERTAR)
    op = input("Opcion: ").strip()

    if op == "1":
        code = input("Codigo IATA: ").strip().upper()
        name = input("Nombre: ").strip()
        city = input("Ciudad: ").strip()
        country = input("Pais (2 letras): ").strip().upper()
        lat = float(input("Latitud: "))
        lon = float(input("Longitud: "))
        activo = input("Activo (s/n): ").lower() == "s"
        pasajeros = int(input("Pasajeros anuales: "))
        terminales = [t.strip() for t in input("Terminales (separadas por coma): ").split(",")]
        valoracion = float(input("Valoracion (0-5): "))
        notas = input("Notas (intro para dejar vacio): ").strip()
        num_tiendas = int(input("Numero de tiendas: "))
        _id = insertar_uno(code, name, city, country, lat, lon, activo,
                           pasajeros, terminales, valoracion, notas, num_tiendas)
        print("Insertado con id:", _id)

    elif op == "2":
        docs = [
            {
                "code": "TST",
                "name": "Test Airport 1",
                "city": "TestCity",
                "country": "XX",
                "coordenadas": {"lat": 0.0, "lon": 0.0},
                "activo": True,
                "pasajeros_anuales": 1000000,
                "terminales": ["T1"],
                "valoracion": 3.0,
                "notas": "Aeropuerto de prueba 1",
                "servicios": {"wifi": True, "parking": False, "hotel_cercano": False, "num_tiendas": 5}
            },
            {
                "code": "TS2",
                "name": "Test Airport 2",
                "city": "TestCity2",
                "country": "XX",
                "coordenadas": {"lat": 1.0, "lon": 1.0},
                "activo": False,
                "pasajeros_anuales": 500000,
                "terminales": ["T1", "T2"],
                "valoracion": 2.5,
                "notas": None,
                "servicios": {"wifi": False, "parking": True, "hotel_cercano": False, "num_tiendas": 3}
            }
        ]
        ids = insertar_varios(docs)
        print("Insertados", len(ids), "documentos.")


def accion_eliminar():
    print(MENU_ELIMINAR)
    op = input("Opcion: ").strip()

    if op == "1":
        code = input("Codigo IATA a eliminar: ").strip().upper()
        n = eliminar_uno(code)
        print("Documentos eliminados:", n)

    elif op == "2":
        pais = input("Codigo de pais: ").strip().upper()
        confirmar = input("Seguro? (s/n): ").lower()
        if confirmar == "s":
            n = eliminar_varios(pais)
            print("Documentos eliminados:", n)
        else:
            print("Cancelado.")


def accion_modificar():
    print(MENU_MODIFICAR)
    op = input("Opcion: ").strip()

    if op == "1":
        code = input("Codigo IATA: ").strip().upper()
        val = float(input("Nueva valoracion: "))
        n = actualizar_uno(code, val)
        print("Documentos modificados:", n)

    elif op == "2":
        pais = input("Codigo de pais: ").strip().upper()
        n = actualizar_varios(pais)
        print("Documentos modificados:", n)

    elif op == "3":
        code = input("Codigo IATA a reemplazar: ").strip().upper()
        name = input("Nuevo nombre: ").strip()
        notas = input("Nuevas notas: ").strip()
        n = reemplazar_uno(code, name, notas)
        print("Documentos reemplazados:", n)


def accion_consultas_simples():
    print(MENU_CONSULTAS_SIMPLES)
    op = input("Opcion: ").strip()

    if op == "1":
        pais = input("Codigo de pais (ej: ES, US): ").strip().upper()
        docs = consulta_por_pais(pais)
        if not docs:
            print("No se encontraron resultados.")
        for d in docs:
            print(" ", d["code"], "-", d["name"], "| Val:", d["valoracion"], "| Pasajeros:", d["pasajeros_anuales"])

    elif op == "2":
        n = int(input("Cuantos aeropuertos quieres ver: "))
        docs = consulta_mejor_valorados(n)
        for d in docs:
            print(" ", d["code"], "-", d["name"], "(", d["country"], ") | Val:", d["valoracion"])


def accion_consultas_array():
    print(MENU_CONSULTAS_ARRAY)
    op = input("Opcion: ").strip()

    if op == "1":
        terminal = input("Terminal a buscar (ej: T4, International): ").strip()
        docs = consulta_por_terminal(terminal)
        if not docs:
            print("No se encontraron resultados.")
        for d in docs:
            print(" ", d["code"], "-", d["name"], "| Terminales:", d["terminales"])

    elif op == "2":
        n = int(input("Numero exacto de terminales: "))
        docs = consulta_num_terminales(n)
        if not docs:
            print("No se encontraron resultados.")
        for d in docs:
            print(" ", d["code"], "-", d["name"], "| Terminales:", d["terminales"])


def accion_consultas_embebido():
    print(MENU_CONSULTAS_EMBEBIDO)
    op = input("Opcion: ").strip()

    if op == "1":
        minimo = int(input("Minimo de tiendas: "))
        docs = consulta_por_tiendas(minimo)
        if not docs:
            print("No se encontraron resultados.")
        for d in docs:
            tiendas = d.get("servicios", {}).get("num_tiendas", "N/A")
            print(" ", d["code"], "-", d["name"], "| Tiendas:", tiendas)

    elif op == "2":
        docs = consulta_sin_hotel()
        if not docs:
            print("No se encontraron resultados.")
        for d in docs:
            print(" ", d["code"], "-", d["name"])


def accion_agrupacion():
    print("\n--- Estadisticas por pais ---")
    print("{:<8} {:<14} {:<16} {}".format("Pais", "Aeropuertos", "Val. media", "Total pasajeros"))
    print("-" * 58)
    for r in consulta_agrupacion_por_pais():
        print("{:<8} {:<14} {:<16.2f} {}".format(
            r["_id"], r["num_aeropuertos"],
            r["valoracion_media"], r["total_pasajeros"]
        ))


# ─── MENU PRINCIPAL ───────────────────────────────────────────

def menu():
    while True:
        print(MENU_PRINCIPAL)
        op = input("Opcion: ").strip()

        if op == "1":
            accion_insertar()
        elif op == "2":
            accion_eliminar()
        elif op == "3":
            accion_modificar()
        elif op == "4":
            accion_consultas_simples()
        elif op == "5":
            accion_consultas_array()
        elif op == "6":
            accion_consultas_embebido()
        elif op == "7":
            accion_agrupacion()
        elif op == "0":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
