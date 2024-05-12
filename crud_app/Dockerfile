# Usa una imagen base de Python
FROM python:3.9-slim-buster

#Actualizar el indice 
RUN apt-get update && apt-get install -y pkg-config 


# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos al directorio de trabajo
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip3 install -r requirements.txt
#RUN pip3 install --upgrade sqlalchemy

# Copia el codigo fuente al directorio de trabajo
COPY . .

# Expone el puerto 5000 para que la aplicacin Flask pueda ser accedida desde fuera del contenedor
EXPOSE 5000

# Ejecuta la aplicacin Flask
CMD ["python", "app.py"]


