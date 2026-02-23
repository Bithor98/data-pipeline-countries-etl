import sqlite3
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
CSV_FILE = DATA_DIR / "countries_clean.csv"
DB_FILE = DATA_DIR / "countries.db"

# Con esta función nos conecta a la base de datos SQLite, si no existe, se crea automáticamente. Devuelve un objeto de conexión que se utilizará para interactuar con la base de datos.
def create_connection(db_path):
    conn = sqlite3.connect(db_path)
    return conn

# Esta función se encarga de crear la tabla "countries" en la base de datos si no existe. Define la estructura de la tabla con las columnas necesarias para almacenar la información de los países, como el código de país (cca2), nombre común, capital, región, población y área.
def create_table(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cca2 TEXT NOT NULL,
            name_common TEXT NOT NULL,
            capital TEXT,
            region TEXT,
            population INTEGER,
            area REAL
        );
    """)

    conn.commit()

# Esta función se encarga de cargar los datos del DataFrame en la tabla "countries" de la base de datos. Primero, borra cualquier dato existente en la tabla para evitar duplicados. Luego, itera sobre cada fila del DataFrame y ejecuta una consulta SQL para insertar los datos correspondientes en la tabla. Finalmente se confirma la transacción para guardar los cambios en la base de datos.
def load_data(conn, dataframe):

    cursor = conn.cursor()
    # Se borra cualquier dato existente en la tabla para evitar duplicados
    cursor.execute("DELETE FROM countries;")

    for _, row in dataframe.iterrows():
        cursor.execute("""
            INSERT INTO countries (
                cca2, name_common, capital, region, population, area
            )
            VALUES (?, ?, ?, ?, ?, ?);
        """, (
            row["cca2"],
            row["name_common"],
            row["capital"],
            row["region"],
            int(row["population"]),
            float(row["area"]) if row["area"] is not None else None
        ))
    # Se confirma la transacción para guardar los cambios en la base de datos
    conn.commit()

# En el bloque principal del código, se realiza la carga de datos en la base de datos. Primero, se lee el archivo CSV utilizando pandas para obtener un DataFrame con los datos de los países. Luego, se crea una conexión a la base de datos SQLite utilizando la función create_connection. A continuación, se llama a create_table para asegurarse de que la tabla "countries" exista antes de cargar los datos. Después, se llama a load_data para insertar los datos del DataFrame en la tabla. Finalmente, se cierra la conexión a la base de datos y se imprime un mensaje indicando que los datos se han cargado correctamente.
if __name__ == "__main__":

# Se lee el archivo CSV utilizando pandas para obtener un DataFrame con los datos de los países
    df = pd.read_csv(CSV_FILE)

# Normaliza valores NaN a None para que SQLite los entienda correctamente
df = df.where(pd.notnull(df), None)

# Elimina filas con valores nulos o vacíos en campos clave
df = df[df["cca2"].notna()]
df = df[df["cca2"].astype(str).str.strip() != ""]
df = df[df["name_common"].notna()]
df = df[df["name_common"].astype(str).str.strip() != ""]

print(f"Filas a cargar en BD: {len(df)}")

# Se crea una conexión a la base de datos SQLite utilizando la función create_connection
conn = create_connection(DB_FILE)

# Se llama a create_table para asegurarse de que la tabla "countries" exista antes de cargar los datos
create_table(conn)

# Se llama a load_data para insertar los datos del DataFrame en la tabla
load_data(conn, df)

# Se cierra la conexión a la base de datos
conn.close()

# Se imprime un mensaje indicando que los datos se han cargado correctamente.
print("Datos cargados correctamente en la base de datos.")


# "Carga los datos limpios desde un CSV en una base de datos SQLite creando la tabla si no existe y evitando duplicados."