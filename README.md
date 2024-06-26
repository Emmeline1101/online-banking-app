# Online Banking System

This is an Online Banking System created using Django Web Framework. And we intentionally inject 4 exploitable vulnerabilities into the code

## Web Architecture
- Frontend:  HTML
- Backend:   Django
- Database:  SQLite & Redis
  
## Features
* Create a Bank Account.
* Deposit & Withdraw Money
* Initial Balance
* Ability to add Minimum and Maximum Transaction amount restriction
* See the balance after every transaction in the Transaction Report
* Modern UI with Tailwind CSS

## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.7
+ Redis Server
+ Git
+ pip
+ Virtualenv (virtualenvwrapper is recommended)

## Requirements

+ celery==4.4.7
+ Django==3.2
+ django-celery-beat==2.0.0
+ python-dateutil==2.8.1
+ redis==3.5.3

## Project Installation

Run Redis server
```bash
redis-server
```

To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With [virtualenv](https://pypi.python.org/pypi/virtualenv),
```bash
virtualenv venv            # create a virtualenv
source venv/bin/activate   # activate the Python virtualenv 
```

or with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/),
```bash
mkvirtualenv -p python3 {{project_name}}   # create and activate environment
workon {{project_name}}   # reactivate existing environment
```

Clone GitHub Project,
```bash
https://github.com/Emmeline1101/online-banking-app.git

cd online-banking-app
```

Install development dependencies,
```bash
pip install -r requirements.txt
```

Migrate Database,
```bash
python manage.py migrate
```

Run the web application locally,
```bash
python manage.py runserver # 127.0.0.1:8000
```

Create Superuser,
```bash
python manage.py createsuperuser
```

Run Celery
(Different Terminal Window with Virtual Environment Activated)
```bash
celery -A banking_system worker -l info

celery -A banking_system beat -l info
```
## How to relogin the system after the first trial (already install dependencies)
```bash
# active virtualenv
source /path/to/venv/bin/activate

# run server
python manage.py runserver

```

## How to exit
```bash
# exit server
ctrl + C

# close Redis
redis-cli shutdown

# exit virtualenv
deactivate

```
## How to manage data
go to `http://127.0.0.1:8000/admin`
if password is forgotten, try:
```shell
python manage.py changepassword <username>

```
## Images:
![Deposit-Page](https://github.com/Emmeline1101/online-banking-app/blob/main/img/Deposit-Page.png)
#
![Transaction-Report-Page](https://github.com/Emmeline1101/online-banking-app/blob/main/img/Transaction-Report-Page.png)
#
![Withdraw-Page](https://github.com/Emmeline1101/online-banking-app/blob/main/img/Withdraw-Page.png)


