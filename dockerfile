# Usa la imagen oficial de Python como base
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo el archivo de dependencias al contenedor
COPY requirements.txt .

# Instala dependencias del sistema (si es necesario) y luego las de Python
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc libpq-dev && apt-get clean

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Expone el puerto 5000 para la API Flask
EXPOSE 5000

# Cambia a un usuario no root por seguridad
RUN adduser --disabled-password appuser
USER appuser

# Define el comando por defecto para ejecutar la API
CMD ["python", "app.py"]
