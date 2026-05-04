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