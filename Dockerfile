# Primera etapa: Construcción y preparación del entorno
FROM python:3.8-slim as builder

# Establece el directorio de trabajo
WORKDIR /app

# Copia solo el archivo de requerimientos
COPY requirements.txt .

# Instala las dependencias en un directorio de sistema virtual
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

# Segunda etapa: Creación de la imagen final
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el entorno virtual con las dependencias
COPY --from=builder /venv /venv

# Copia el resto del código fuente
COPY . .

# Expone el puerto que utiliza Flask
EXPOSE 5000
EXPOSE 9100

# Ejecuta la aplicación
CMD ["/bin/bash", "-c", "/app/node_exporter & /venv/bin/python app.py"]
