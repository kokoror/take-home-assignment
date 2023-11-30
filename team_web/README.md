
This web app requires installation of MySQL (server and workbench) on your local machine, for installation, please refer to the offical documentation at https://dev.mysql.com/doc/mysql-getting-started/en/ 
and tutorial made by Web Dev Simplified on Youtube at https://www.youtube.com/watch?v=u96rVINbAUI&ab_channel=WebDevSimplified   

# Step 1: Clone the Repository
Create a local directory, run `git clone ` to clone the repository to your local directory.

# Step 2: Set up a Python virtual environment:
Run `python -m venv venv` to create a virtual environment for the app, then run `source venv/bin/activate` (if on Unix/Mac) or `venv\Scripts\activate` (if on Windows) to activate it.

# Step 3: Install Python Dependencies
I have included all the Python dependencies required for the app in the file dependencies.txt. Simply run `pip install -r dependencies.txt` to install all of them.

# Step 4: Set up environment variables for the web app
Create a `.env` file in the root directory of the project - where manage.py is located, paste the below environment variables in this file and change the values as needed. The file should include the following varibales for MySQL connection.

#include below in .env file
#the value should reflect your MySQL settings on your machine, 
DB_NAME=djangoapp #name anything for the database used for this web app
DB_HOST=localhost #by default this should be localhost
DB_USER=root #your local db user name
DB_PASS=000000 #your local db password
DB_PORT=3306 #your db port number

# Step 5: Set up database
Run `python manage.py migrate` in the terminal to set up tables in MySQL.
Run `python manage.py createsuperuser` to create an admin account.

# Step 6: Start the server
Run `python manage.py runserver` in the terminal to start the server

# Step 7: Run the application
Head to `http://localhost:8000/` , you should see the website's home page with an empty list of team members


# RUN TEST
Run 'python manage.py test' in the terminal to run unit tests for the components for this app. All tests are defined in ./team_web/test.py.

# Estimated time spent on this application
I have spent 4 days dedicating 3~5 hours/day to this application. This include a quick ramp up on Django framework, setting up the environment, implementing the logic, debugging and testing the app, compiling a documentation, pushing to github and dry running the build for this app. 




