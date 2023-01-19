
# Command ran in pipeline
run-tests: install-requirements
	python3 -m pytest ./tests/ -p no:warnings -vv 

install-requirements:
	pip3 install -r ./tests/test-requirements.txt

# Command ran locally
test-api:
	python3 -m pytest ./tests/ -p no:warnings -vv 