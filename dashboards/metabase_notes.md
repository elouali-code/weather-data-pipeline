#  Metabase Dashboard Notes

## Overview

This document describes how to run and access the Metabase dashboard for the Weather Data Pipeline project.

---

##  Launch Metabase

Make sure Java is installed, then run:

```bash
java -jar metabase.jar
```

Metabase will start at:

http://localhost:3000

---

##  Database Connection

During Metabase setup:

* Database type: SQLite
* Database file: `data/warehouse/weather_sqlite.db`

---

##  Available Visualizations

The dashboard **Weather Analytics Dashboard** includes:

* Temperature trend by city (line chart)
* Average temperature by city (bar chart)
* Average humidity by city (bar chart)
* Detailed weather table with filters

---

##  Purpose

The dashboard provides quick insights into weather patterns across multiple cities and demonstrates end-to-end data pipeline capabilities.

---

##  Notes

* Data is refreshed via the Python ETL pipeline.
* Raw data is stored in JSON format.
* Curated data is stored in SQLite.
