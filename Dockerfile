FROM python:3.11-slim

WORKDIR /app

# copier requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copier le projet
COPY . .

CMD ["python", "etl.py"]