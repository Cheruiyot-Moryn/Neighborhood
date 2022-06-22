# Neighborhood

## Author
Moureen Chepkoech

### Description
This a Django application where a user can post a project and the projects can be viewed and rated according to the criteria given. The user can also click the link button to view what the project contains.

## Setup and Installations
To get the code, clone the repository: https://github.com/Cheruiyot-Moryn/Neighborhood.git
and run the following commands;

    $ cd Neighborhood
    $ pip install -r requirements.txt

### Install and actiavte the virtual environment

    $ python3.8 -m venv env 
    $ source env/bin/activate

### Create a database

    $ psql
    $ CREATE DATABASE (name_of_database);

### Make migrations

    $ python3.8 manage.py check
    $ python3.8 manage.py makemigrations (app_name)
    $ python3.8 manage.py migrate 

### Testing the Application 

    $ python3.8 manage.py test (app_name)

### Running the Application 

    $ python3.8 manage.py runserver

Then once you are done, open your browser with the local host; 127.0.0.1:8000

## Dependencies
1. Python
2. Django
3. Virtual environment 
4. Heroku
5. Gunicorn

## Technologies Used
1. Python
2. HTML
3. Django
4. Bootstrap 3
5. Heroku
6. Postgresql

# Live Link
[View Live Site.](https://pioneerhood.herokuapp.com/)

## License
Awwards-Show is under the [MIT](LICENSE) license.
