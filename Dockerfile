# Usa una imagen oficial de Python como imagen base
FROM python:3.13.0rc3-alpine3.19

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios en el contenedor

COPY ruta2/. /app/ruta2
COPY endpoint1.html /app
COPY endpoint1_2.html /app
COPY index_basico.html /app
COPY index.html /app
COPY requirements.txt /app
COPY server.py /app
COPY main.py /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación escuchará
EXPOSE 8432

# Comando para ejecutar la aplicación
CMD ["python", "/app/server.py"]