# TASCO E-COMMERCE

## Installation of pre-requisites

1. Python3.6, Python3.6-dev
1. virtualenv
1. PostgreSQL

If you have all the pre-requisites installed, skip this step and go to next step

### Install Python3.6

```sh
sudo apt-get install python3.6 python3.6-dev
python3 --version
```

### Install virtualenv

```sh
sudo apt-get install virtualenv
virtualenv --version
```

### Install PostgreSQL

```sh
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install postgresql postgresql-contrib
psql --version

# you can install pgadmin3 optionally to explore database
sudo apt-get install pgadmin3
```

## Setup PostgreSQL database

```sh
# enter postgresql cli
sudo su postgres
psql
```

```sql
/* see the list of users with their roles/attributes */
\du

/* create a new user if you do not want to use existing users */
CREATE USER <username> WITH PASSWORD <password>;

/* give the new user superuser role */
ALTER USER <username> WITH ROLE SUPERUSER;

/* create new database with one of the users as owner */
CREATE DATABASE <database-name> WITH OWNER=<username>;
```

## Project Setup

```sh
# go to project root after cloning the project
cd PATH_TO_PROJECT_ROOT

# create virtual environment with python3.6 as default python and activate it
virtualenv -p python3.6 .venv
source .venv/bin/activate
# For windows
.\.venv\Scripts\activate

# install api dependecies
pip install -r requirements.txt

# copy example env containing necessary environment variables to .env
cp env.example .env
```

open `.env` and input values of following variables

```env
DJANGO_SECRET
DATABSE_NAME
DATABSE_OWNER
DATBASE_PASSWORD
```

complete setup with the following commands

```sh
# run database migration
python manage.py migrate


# create admin user
python manage.py createsuperuser

# load data
python manage.py runscript loadsettingsdata

python manage.py runserver
```
