### Run API Locally ###################
run-api: 
	uvicorn src.backend.api.app:api --reload
######################################


### Add Dependencies to Requirements #
add-deps-backend:
	pip3 freeze -l > src/backend/requirements.txt 

add-deps-tests:
	pip3 freeze -l > src/backend/tests/requirements.txt
#######################################


### Docker shortcuts #################
docker-up: docker-compose-build
	docker-compose up

docker-down: docker-compose-down
	docker image rm dark-knight_website-api dark-knight_database dark-knight_astack-finance-service dark-knight_astack-authenticator-service dark-knight_astack-rosters-service dark-knight_astack-welcome-service dark-knight_astack-scheduletipper-service dark-knight_ymbl-site-query-api
	
docker-compose-build:
	docker-compose build 

docker-compose-down:
	docker-compose down 
#######################################