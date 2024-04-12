# Usa una imagen base oficial de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el resto del código fuente
COPY . .

# Expone el puerto que utiliza Flask
EXPOSE 5000

# Ejecuta la aplicación
CMD ["python", "app.py"]
