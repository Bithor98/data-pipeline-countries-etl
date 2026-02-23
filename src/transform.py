from pathlib import Path
import json
import pandas as pd

DATA_DIR = Path("data")
RAW_FILE = DATA_DIR / "raw_countries.json"
CLEAN_FILE = DATA_DIR / "countries_clean.csv"

def transform_countries(raw_data):
    """
    Transforma los datos crudos obtenidos de la API REST Countries
    en un DataFrame limpio y estructurado.

    Columnas resultantes:
    - cca2: código del país
    - name_common: nombre común
    - capital: capital del país
    - region: región geográfica
    - population: población
    - area: superficie
    """
    rows = []

    for item in raw_data:
        cca2 = item.get("cca2")

        # name is nested: {"name": {"common": "...", ...}}
        name_common = (item.get("name") or {}).get("common")

        # capital can be missing or list
        capital_list = item.get("capital") or []
        capital = capital_list[0] if isinstance(capital_list, list) and len(capital_list) > 0 else None

        region = item.get("region")
        population = item.get("population")
        area = item.get("area")

        rows.append(
            {
                "cca2": cca2,
                "name_common": name_common,
                "capital": capital,
                "region": region,
                "population": population,
                "area": area,
            }
        )

    df = pd.DataFrame(rows)

    # Basic cleanup
    df = df.dropna(subset=["cca2", "name_common"])  # key fields
    df["cca2"] = df["cca2"].astype(str).str.upper().str.strip()
    df["name_common"] = df["name_common"].astype(str).str.strip()
    df["region"] = df["region"].astype("string").str.strip()
    df["capital"] = df["capital"].astype("string").str.strip()

    # Ensure numeric types when possible
    df["population"] = pd.to_numeric(df["population"], errors="coerce").fillna(0).astype("int64")
    df["area"] = pd.to_numeric(df["area"], errors="coerce")

    # Remove duplicates by country code (keep first)
    df = df.drop_duplicates(subset=["cca2"]).reset_index(drop=True)

    return df


# tu función transform_countries se queda IGUAL

if __name__ == "__main__":
    with open(RAW_FILE, encoding="utf-8") as f:
        raw = json.load(f)

    df = transform_countries(raw)

    DATA_DIR.mkdir(exist_ok=True)
    df.to_csv(CLEAN_FILE, index=False)

    print(f"Datos limpios guardados en {CLEAN_FILE}")
    print(f"Filas guardadas: {len(df)}")