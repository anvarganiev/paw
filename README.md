Project Auction of KPFU
=============================


Instalation
------------
	git clone https://github.com/anvarganiev/paw
    
Requirements
------------
postgresql

You can work in global python enviroment if you want to,
but it will be better to work in virtual environment

	pip3 install virtualenv
    virtualenv djangoenv
    source djangoenv/bin/activate

The minimum python requirements by this project is in requirements.txt

	pip3 install -r requirements.txt

Quick start
------------
basic django commands:

    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py migrate --fake-initial
    python3 manage.py migrate --run-syncdb
    python3 manage.py runserver
    python3 manage.py createsuperuser
