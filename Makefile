PY38 := $(shell which python3.8)

setup:
	$(PY38) -m venv ~/.flask-ml-azure38
	@echo "Run 'source ~/.flask-ml-azure38/bin/activate' to activate the environment."

install:
	~/.flask-ml-azure38/bin/pip install --upgrade pip &&\
	~/.flask-ml-azure38/bin/pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W0702 app.py

docker-build:
	docker build -t my-python-flask-app .

docker-run:
	docker run -p 5002:5002 my-python-flask-app

docker-debug:
	docker run -d -p 5002:5002 --name my-flask-container my-python-flask-app
	docker exec -it my-flask-container bash

docker-clean:
	if [ -n "$$(docker images -aq)" ]; then \
		docker rmi -f $$(docker images -aq); \
	fi

all: install lint
