Para el backend, la aplicacion flask; en el archivo docker-compose.yml se puede agregar variables de entorno

EL PROCESO DE DOCKER COMPOSE ES EL SIGUIENTE
1. Al crearse o iniciar el contenedor se crean la variables de entorno declaradas en "environ", estas variables pueden reemplazar a las de Dockerfile. OJO, tiene que especificarse primero la ruta del archivo .env
2. Las variables de entorno que le pasemos en el archivo Dockerfile con ENV; internamente va a crear un archivo .env con esas variables.