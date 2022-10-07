install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black Likes/*.py Quotes/*.py Likes/Likes/*.py Quotes/Quotes/*.py Likes/likes/*.py Quotes/quotes/*.py
lint:
	#flake8 or # pylint
	pylint --disable=R,C Likes/*.py Quotes/*.py Likes/Likes/*.py Quotes/Quotes/*.py Likes/likes/*.py Quotes/quotes/*.py
test:
	#test
	python Quotes/manage.py test
	python Likes/manage.py test
build:
	#containerization
	#docker build -t deploy-fastapi .
run:
	#run docker image
deploy:
	# run deploy commands

all: install lint test deploy