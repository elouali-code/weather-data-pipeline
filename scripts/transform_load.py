import os
import json
import pandas as pd
import duckdb

raw_path = "../raw"
records = []

for file in os.listdir(raw_path):
    if file.endswith(".json"):
        city = file.replace(".json", "").capitalize()
        
        with open(os.path.join(raw_path, file)) as f:
            data = json.load(f)
        
        # wttr structure
        weather_days = data["weather"]
        
        for day in weather_days:
            records.append({
                "city": city,
                "date": day["date"],
                "avg_temp_c": float(day["avgtempC"]),
                "max_temp_c": float(day["maxtempC"]),
                "min_temp_c": float(day["mintempC"]),
                "humidity": float(day["hourly"][0]["humidity"])
            })

# DataFrame
df = pd.DataFrame(records)

print("Data preview:")
print(df.head())

# Save into DuckDB
con = duckdb.connect("../weather.db")

con.execute("""
CREATE TABLE IF NOT EXISTS weather AS
SELECT * FROM df
""")

print("Chargement dans DuckDB terminé ")

import sqlite3

sqlite_con = sqlite3.connect("../weather_sqlite.db")
df.to_sql("weather", sqlite_con, if_exists="replace", index=False)

print("Export vers SQLite terminé ")