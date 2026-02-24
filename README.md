# 🌦️ End-to-End Weather Data Pipeline

## Overview

This project demonstrates a complete end-to-end data engineering pipeline that ingests weather data from a public API, transforms it, stores it in a data warehouse, and visualizes insights using Metabase.

The goal is to showcase production-style data engineering skills suitable for a junior data engineer role.

---

##  Architecture

Weather API → Python Extract → Raw JSON → Pandas Transform → SQLite Warehouse → Metabase Dashboard

---

##  Tech Stack

* Python
* Pandas
* DuckDB
* SQLite
* Metabase
* REST API

---

##  How to Run

### 1. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run extraction

```bash
python scripts/extract_weather.py
```

### 4. Run transformation & load

```bash
python scripts/transform_load.py
```

### 5. Launch Metabase

```bash
java -jar metabase.jar
```

Then connect to:

```
data/warehouse/weather_sqlite.db
```

---

##  Dashboard Features

* Temperature trend by city
* Average temperature comparison
* Average humidity by city
* Interactive filtering

---

##  Skills Demonstrated

* API ingestion
* ETL pipeline design
* Data transformation
* Data warehousing
* Business Intelligence
* End-to-end data workflow

---

##  Author

Abderrahman Elouali
