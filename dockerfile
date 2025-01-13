# Usa la imagen oficial de Python como base
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias (requirements.txt) al contenedor
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Expone el puerto 5000 para la API Flask
EXPOSE 5000

# Define el comando por defecto para ejecutar la API
CMD ["python", "app.py"]
