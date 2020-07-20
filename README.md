Comparte Ride
=============

Group-bounded, invite-only, carpooling platform


Comandos:

docker-compose -f local.yml build
docker-compose -f local.yml down
docker-compose -f local.yml up
docker-compose -f local.yml ps

Variable de entorno en la terminal
export COMPOSE_FILE=local.yml

Despues de hacer esto los comando son

docker-compose build
docker-compose down
docker-compose up
docker-compose ps

Comandos administrativos (se deve crear la variable de entorno)

docker-compose run --rm django python manage.py createsuperuser


Hablitar un contenedor por separado

docker rm -f <ID> (para matar Django)

docker-compose run --rm --service-ports django (para correr django aparte)