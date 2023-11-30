# Documentation
(Please note `raoqiange` and `kokoror` both are my personal github accounts, I have set up my local git to use `raoqiange` by default, that's why you are seeing `raoqiange`'s commits on `kokoror`'s repository here. Sorry about the confusion.)

This web app requires installation of MySQL (server and workbench) on your local machine, for installation, please refer to the offical documentation at https://dev.mysql.com/doc/mysql-getting-started/en/ 
and tutorial made by Web Dev Simplified on Youtube at https://www.youtube.com/watch?v=u96rVINbAUI&ab_channel=WebDevSimplified   

## Step 1: Clone the Repository
Run `git clone https://github.com/kokoror/take-home-assignment.git` to clone the repository to your local directory. Then, cd into the repo directory by running `cd take-home-assignment`.

## Step 2: Set up a Python virtual environment:
In the root directory of your local repository, run `python -m venv venv` in terminal to create a virtual environment for the app, then run `source venv/bin/activate` (if on Unix/Mac) or `venv\Scripts\activate` (if on Windows) to activate it.

## Step 3: Install Python Dependencies
I have included all the Python dependencies required for the app in the file dependencies.txt. Simply run `pip install -r dependencies.txt` to install all of them.

## Step 4: Set up environment variables for the web app
Update `.env` file in the root directory of the project - where manage.py is located, the file should contain the below environment variables for MySQL connection, change the values as needed.

```
#update the below env variable values in the .env file
#the value should reflect your MySQL settings on your machine, 
DB_NAME=djangoapp #name anything for the database used for this web app
DB_HOST=localhost #by default this should be localhost
DB_USER=root #your local db user name
DB_PASS=000000 #your local db password
DB_PORT=3306 #your db port number
```

## Step 5: Set up database
Before proceeding, please make sure your local MySQL has been set up and the MySQL server is running on your machine.
In the root directory of this repository, follow the below steps: 
1. Run `python db.py` in the terminal to setup the database used for this web app.
2. Run `python manage.py migrate` in the terminal to set up tables in MySQL.
3. Run `python manage.py createsuperuser` to create an admin account. (by doing this, you are able to have access to the admin site at `http://localhost:8000/admin` to interact with the db through user interface in order to add, update, delete the content on the Django app)

## Step 6: Start the server
Run `python manage.py runserver` in the terminal to start the server.

## Step 7: Run the application
Head to `http://localhost:8000/` , you should see the website's home page with an empty list of team members,


# RUN TEST
Run `python manage.py test` in the terminal to run unit tests for the components for this app. All tests are defined in ./team_web/test.py.
CTRL + C to stop the server

# Estimated time spent on this application
I have spent 4 days dedicating 3~5 hours/day to this application. This include a quick ramp up on Django framework, setting up the environment, implementing the logic, debugging and testing the app, compiling a documentation, pushing to github and dry running the build for this app. 





