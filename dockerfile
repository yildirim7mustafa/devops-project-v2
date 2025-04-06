# Resmi Python image'ını kullan
FROM python:3.12

# Çalışma dizinini belirle
WORKDIR /app

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Port tanımla
EXPOSE 8000

# Uvicorn ile FastAPI uygulamasını başlat
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
