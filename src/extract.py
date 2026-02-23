import requests
import json
from pathlib import Path

API_URL = (
    "https://restcountries.com/v3.1/all"
    "?fields=name,population,region,capital,area,cca2"
)

DATA_DIR = Path("data")
RAW_FILE = DATA_DIR / "raw_countries.json"

def fetch_countries_data():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    return response.json()

def save_raw_data(data):
    DATA_DIR.mkdir(exist_ok=True)
    with open(RAW_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    data = fetch_countries_data()
    save_raw_data(data)
    print(f"Datos crudos guardados en {RAW_FILE}")
    print(f"Número de países: {len(data)}")