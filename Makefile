run:
	docker-compose down
	docker-compose build
	docker-compose up

build:
	docker build balance/ --tag emilrakhimov/balance:latest

start: build
	docker run --detach --name server -p 8080:8080 --rm --volume 'pwd':/var/log emilrakhimov/balance:latest

stop:
	docker stop server 
	
clean:
	docker rmi -f emilrakhimov/balance:latest
	docker rm emilrakhimov/balance:latest

healthcheck:
	@which docker || echo "docker is not installed"
	@which docker-compose || echo "d-c is not installed"

.PHONY: build up stop healthcheck

