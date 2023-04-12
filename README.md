## Sample FastAPI app

> after cloning the source code
### Setup

##### Python 3.8 and Redis

```commandline
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.8
$ sudo apt-get install redis-server
```

##### Pip3
```commandline
$ sudo apt install python3-pip
```

##### Pipenv
```commandline
$ pip3 install pipenv
```
> _assuming following commands are executing in project, after clone from gitlab._

##### Creating environment file
Update the .env file with respective values. Add environment variables in this file.
Important to put values for database config. 
Re-enable the virtual environment after adding the env variables in .env file.
```commandline
$ cp sample.env .env
```

##### Create virtual env and Install Packages

The first time it will check in `~/.virtualenvs` virtual environments folder whether a virtual environment is present for this application, 
if not pipenv will automatically create a new virtual environment

```commandline
$ pipenv install
```

for development dependencies
```commandline
$ pipenv install --dev
```

##### Enable virtual environment

Enabling the virtual env.

```commandline
$ pipenv shell
```

##### Updating database schema

Use [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html#running-our-first-migration) if there is any add/delete/update in database models.
> _Run following command to run db upgrade, and create tables in database. Assuming all db related environment variables are set in .env file and don't forget to create an empty database for the first time before running below command._ 
```commandline
$ alembic upgrade head
$ alembic downgrade base  # To downgrade the database models
$ alembic downgrade -1  # To undo last migration
```


##### Seeding database with sample data. (optional)
To seed all the tables in all schemas
Make sure to set pythonpath to root directory and mark the app and base folder as root before running the below command.
```commandline
$ python ./db-migration/seed/__init__.py
```

Start server with gunicorn
```commandline
$ uvicorn main:fast_app --reload
```
