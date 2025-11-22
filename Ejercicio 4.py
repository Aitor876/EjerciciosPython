import csv
import requests
from collections import defaultdict

url = "https://fixturedownload.com/download/la-liga-2025-UTC.csv"
archivo = "la-liga-2025.csv"

print("Descargando resultados de La Liga 2025...")
response = requests.get(url)
response.raise_for_status()
with open(archivo, "wb") as f:
    f.write(response.content)
print(" Archivo CSV descargado adecuadamente.\n")

equipos = defaultdict(lambda: {"GF": 0, "GC": 0, "PTS": 0})

with open(archivo, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    home_col = next(c for c in reader.fieldnames if "home" in c.lower() or "team 1" in c.lower())
    away_col = next(c for c in reader.fieldnames if "away" in c.lower() or "team 2" in c.lower())
    result_col = next(c for c in reader.fieldnames if "result" in c.lower())

    for fila in reader:
        if not fila[result_col] or '-' not in fila[result_col]:
            continue

        home = fila[home_col].strip()
        away = fila[away_col].strip()
        goles_home, goles_away = map(int, fila[result_col].split('-'))

        equipos[home]["GF"] += goles_home
        equipos[home]["GC"] += goles_away
        equipos[away]["GF"] += goles_away
        equipos[away]["GC"] += goles_home

        if goles_home > goles_away:
            equipos[home]["PTS"] += 3
        elif goles_home < goles_away:
            equipos[away]["PTS"] += 3
        else:
            equipos[home]["PTS"] += 1
            equipos[away]["PTS"] += 1

print("=== Goles a favor ===")
for equipo, datos in equipos.items():
    print(f"{equipo:25} {datos['GF']} goles")

clasificacion = sorted(
    equipos.items(),
    key=lambda x: (
        -x[1]["PTS"],
        -(x[1]["GF"] - x[1]["GC"]),
        -x[1]["GF"],
        x[0]
    )
)

print("\n=== Clasificación final ===")
for i, (equipo, datos) in enumerate(clasificacion, start=1):
    dif = datos["GF"] - datos["GC"]
    print(f"{i:2}. {equipo:25} PTS: {datos['PTS']:2} GF: {datos['GF']:3} GC: {datos['GC']:3} DG: {dif:3}")
