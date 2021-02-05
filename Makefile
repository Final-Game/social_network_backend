#!make
include ./envs/dev.env
export $(shell sed 's/=.*//' ./envs/dev.env)


start_infra:
	docker-compose -f docker-compose.infra.yml up --build -d

shutdown_infra:
	docker-compose -f docker-compose.infra.yml down

start: 
	docker run willwill/wait-for-it percona-xtradb-cluster:3306 -t 15 -- echo "Connect to database successful."
	docker-compose build
	docker-compose run --rm cms-admin python manage.py migrate
	docker-compose up --build -d

shutdown:
	docker-compose down

start_all:
	echo "Start infrastructure..."
	make start_infra
	echo "Start App..."
	make start

shutdown_all:
	echo "Shutdown App..."
	make shutdown
	echo "Shutdown infrastructure..."
	make shutdown_infra