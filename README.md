# The Avengers Initiative
Python/Flask-based Team Management App

## Get Files
Clone or download this repo and rename to your desire

## Setup
Configure database settings in `/instance/config.py`
Edit the settings to reflect your own, i.e `SQLALCHEMY_DATABASE_URI = 'mysql://database_username:database_password@localhost/payaya'`

## Running
### Bash Commands
Navigate into the project directory i.e `cd avengers-initiative`
All our bash commands will be made from this directory.

### Virtual Environment
Drop into the virtual environment by typing `virtualenv venv`
Activate the virtual env by typing `. venv/bin/activate`

### Export App
To set up the app environment, type `export FLASK_APP=run.py`

### Start Server
Type `flask run` to get the Flask Server running

You'll be provided with a link to view the app in your browser