# syntax=docker/dockerfile:1

# Imagen base ligera de Python
FROM python:3.10-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar el código fuente al contenedor
COPY src/ ./src/
COPY requirements.txt .

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8080
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
