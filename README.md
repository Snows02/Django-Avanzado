## **Comandos:**

  

 1. docker-compose -f local.yml build
 2. docker-compose -f local.yml down
 3.  docker-compose -f local.yml up
 4.  docker-compose -f local.yml ps
      

## Variable de entorno en la terminal

 - export COMPOSE_FILE=local.yml

Después de hacer esto los comando son

 1. docker-compose build
 2. docker-compose down
 3. docker-compose up
 4. docker-compose ps
  

## **Comandos administrativos (se debe crear la variable de entorno)**

 1. docker-compose run --rm django python manage.py createsuperuser
  
**

## Hablitar un contenedor por separado

**

 1. docker rm -f <ID> (para matar Django)
 2. docker-compose run --rm --service-ports django (para correr django aparte)