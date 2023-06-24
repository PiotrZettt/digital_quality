# Digital Quality
A digital inspection SaaS app

## Setup project

Create a new folder and clone the repo.
```commandline
git clone git@github.com:PiotrZettt/digital_quality.git
```

Create and activate a python virtual environment
```commandline
python3 -m venv venv
source venv/bin/activate
```

You will also need a .env file to store your sensitive environmental variables.
```commandline
touch .env && open .env
```

Set the variables like so:


ALLOWED_HOSTS=* \
DEBUG=on \
SECRET_KEY='some_string' \
PYTHONBUFFERED=1

Save and close the file

You are ready now to install the requirements.
Create a requirements-dev.txt
```commandline
touch requirements-dev.txt && open requirements-dev.txt
```
Add: \
pip-tools \
pre-commit 

Save and close the file.

Install the dev tools:
```commandline
pip install -r requirements-dev.txt
```

Compile the requirements.txt file by 
```commandline
pip-compile
```
Install the requirements.txt
```commandline
pip install -r requirements.txt
```

Install the pre-commit tools:
```commandline
pre-comit install
```

Now with every commit attempt a set of checks will be performed.

Before you can run the project you will need to config the database in settings.py - 'DATABASES'. \
Create a Postgres database and put all the credentials including name, username, host, password and port number.

The app uses the django-tenant package to provide a multi-tenant functionality.
Please read the django-tenant documentation for further details.

To run the app: \
```commandline
python manage.py runserver
```
