# Digital Quality
A digital inspection SaaS app.

The app provides useful quality inspection tools like audits and PDI forms, stock movement and quality analysys.
At the moment there are three modules of "Stock Flow", "Pre Delivery Inspection" and "Internal Audits."
The app is based on multi-tenant - shared database - isolated schema approach. Each user will have their own subdomain
and their own DB schema created for data isolation.

## TODO

- [x] Install Requirements
- [x] Setup Pre-commit
- [x] Setup Postgres DB
- [ ] Setup testing
- [x] Create multi-tenant based on a DB Schema functionality
- [ ] User/Tenant creation and log-in
- [ ] Email account verification
- [ ] Create and add user permissions
- [ ] All-Auth integration (optional)
- [x] Modelling data for:
    - [x] Stock Flow module
    - [x] Audits module
    - [x] PDI module
- [ ] Create API serializers and views
- [ ] Build the Frontend:
    - [ ] Home Page
    - [ ] User/Tenant creation
    - [ ] Login
    - [ ] Your Company Profile
      - [ ] Your Staff
      - [ ] Your Stock
      - [ ] Your Audits
      - [ ] Your PDIs
    - [ ] Your Dashboard
    - [ ] Your Customer Dashboard
- [ ] Setup Gunicorn
- [ ] Deploy

## Setup project

You will need a gmail account for testing the email functionality of the application.

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

EMAIL_ID='your-gmail-address' \
EMAIL_PW='your-gmail-password'

Save and close the file

You are ready now to install the requirements.

```
pip install -r requirements-dev.txt
```

Compile the requirements.txt file by
```commandline
pip-compile requirements.in
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

To run the app:
```commandline
python manage.py runserver
```
