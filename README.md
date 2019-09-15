# HoodWatch

### 13/09/2019

## By **[Brian Sunday](https://github.com/Sundaybrian/hood-watch)**

## Description

 web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## User Stories

As a user I would like:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : john@doe.com  Username : jonDoo  Password : doe | New user is registered |
| User Log in | Your email : john@doe.com  Password : doe | Logged in |
| Create Post | Click Add Button |Authenticated User is redirected to a form page to create a new post|
| View Post | Click on Post title | Redirected to a page that has that single post|
| Update a Post | Click Update Icon| Authenticated user i.e owner of the post is redirected to a form field to update the post|
| View Businesses | Click businesses| Authenticated User is redirected to a page of all businesses in their neighbourhood |
| Update profile | Click edit profile | Pop up modal to update your details |
| Search Posts | Submit query in search field | Redirected to a search results page and displayed your query search results|


## Setup/Installation Requirements

* `$ git clone` [NeighbourhoodWatch](https://github.com/Sundaybrian/hood-watch)
* `$ cd prodev`


    ```python
    #create a .env file
    SECRET_KEY = '<Secret_key>'
    DBNAME = 'hoodwatch'
    USER = '<username>'
    PASSWORD = '<password>'
    DEBUG = True

    
    ```    

* `$ python3.6 -m venv virtual` to create a  virtual environment
* `$ source virtual/bin/activate` to activate the virtual environment
* `$ psql` to activate the postgres server
* `$ username=create database hoodwatch` create db with the name prodev2
* run `$ python3.6 -m pip install -r requirements.txt ` to install dependencies
* `$ python3.6 manage.py makemigrations` to initialize database migrations
* `$ python3.6 manage.py migrate` to commit the migration you are running
* `$ python3.6 manage.py runserver` to run the app
* open `localhost:8000` to view the app

## Known Bugs

* No known Bugs

## Technologies Used

* Python3.6
* Django 2.2.4
* Javascript
* Masonry Grid
* Bootstrap
* Postgres Database
* CSS
* HTML
* Heroku

### License

MIT (c) 2019 **[Brian Sunday](https://github.com/Sundaybrian/hood-watch)**

