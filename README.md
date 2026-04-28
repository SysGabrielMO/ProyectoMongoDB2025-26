# Proyecto MongoDB – Aeropuertos Mundiales

## Descripción

Proyecto de base de datos NoSQL con MongoDB usando una colección de aeropuertos mundiales.
El JSON base se obtuvo de `https://jsonlint.com/datasets/airports.json` y fue modificado
para incluir todos los tipos de datos soportados por MongoDB.

---

## Estructura del proyecto

```
proyecto/
├── aeropuertos.json       # Colección de datos para importar
├── funciones.py           # Funciones de acceso a la base de datos
├── menu.py                # Menú principal de la aplicación
└── README.md
```

---

## Instalación de MongoDB en Debian 13

```bash

# 1. Descargar paquetes
wget https://repo.mongodb.org/apt/debian/dists/bookworm/mongodb-org/7.0/main/binary-amd64/mongodb-org-server_7.0.22_amd64.deb
wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-debian12-x86_64-100.10.0.deb

# 2. Instalamos los paquetes que hemos descargado con:
dpkg -i mongodb-org-server_7.0.22_amd64.deb
dpkg -i mongodb-database-tools-debian12-x86_64-100.10.0.deb

# 3. Arrancar el servicio
sudo systemctl start mongod
sudo systemctl enable mongod

# 6. Verificar que funciona
sudo systemctl status mongod
mongoimport --version
```

---

## Importar la colección

```bash
mongoimport --db aeropuertos_db --collection aeropuertos --file aeropuertos.json --jsonArray
```

---

## Instalar dependencias Python

```bash
pip install pymongo
```

## Ejecutar la aplicación

```bash
python3 menu.py
```
