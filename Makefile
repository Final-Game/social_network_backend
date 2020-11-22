start: 
	export `cat ./envs/dev.env | xargs` && docker-compose up --build -d

shutdown:
	export `cat ./envs/dev.env | xargs` && docker-compose down