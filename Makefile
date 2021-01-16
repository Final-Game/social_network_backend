#!make
include ./envs/dev.env
export $(shell sed 's/=.*//' ./envs/dev.env)


start_infra:
	docker-compose -f docker-compose.infra.yml up --build -d

shutdown_infra:
	docker-compose -f docker-compose.infra.yml down

start: 
	docker-compose up --build -d

shutdown:
	docker-compose down

start_all:
	make start_infra && make start

shutdown_all:
	make shutdown && make shutdown_infra