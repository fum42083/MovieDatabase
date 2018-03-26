required:

python 2.7
django 1.11
imdbpie
rabbitmq-server

install:

pip install django
apt-get install rabbitmq-server
pip install celery
pip install imdbpie

Run:

Start celery worker: celery worker --app MovieDatabase --loglevel=INFO (run in project folder)
Start rabbitmq: service rabbitmq-server start
run django: python manage.py runserver
