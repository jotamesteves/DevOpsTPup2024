## ** DevOpsTPup2024 **
Descripción del Proyecto
Este repositorio contiene un proyecto de DevOps para la Universidad de Palermo, destinado a implementar una aplicación Flask con monitoreo utilizando Prometheus y Grafana.

## Requisitos
- Git
- Docker
- Docker Compose

## Instalación
Para instalar y ejecutar el proyecto, sigue estos pasos:

1. Clonar el repositorio:
`git clone https://github.com/jotamesteves/DevOpsTPup2024.git`
2. Navegar al directorio del proyecto:
`cd DevOpsTPup2024`
3. Asegurarse de que Docker está encendido.
`docker ps`
4. Levantar los servicios con Docker Compose:
`docker-compose up`

## Uso
- Aplicación Flask: http://localhost:5001
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## Endpoints
- /: Devuelve "Hola Mundo".
- /error: Simula un error con código 500.
- /mantenimiento: Indica que el sitio está en mantenimiento.

##Monitoreo
Prometheus recopila métricas desde la aplicación Flask y node_exporter. Estas métricas se pueden visualizar en Grafana.

##Pruebas
Para ejecutar las pruebas con pytest, utiliza el siguiente comando:
`pytest`


## Contribuir
Para contribuir a este proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios.
3. Realiza tus cambios.
4. Asegúrate de que las pruebas pasen.
5. Haz commit de tus cambios.
6. Haz push a tu rama.
7. Envía un pull request.


## Licencia
Este proyecto está bajo la licencia MIT.

## Autores y Agradecimientos
Creado por Jota Esteves y Franco Bangert.

