## Capstone project

### Installing Dependencies

# Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

# Virtual Enviornment
Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

# PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:
```
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

# Running the server
From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```
#For windows
set FLASK_APP=app.py

#For mac
export FLASK_APP=app.py;
```

To run the server, execute:

```
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Introdution
- The capstone project follows RESTful principles, including naming of endpoints, use of HTTP methods GET , POST, PATCH and DELETE. The project handles errors using unittest library to test each endpoint for expected behaviour and error handling if applicable.

## Getting Started

- Base URL: At present this app can be run locally and also on heroku. The backend app is hosted at the default, http://127.0.0.1:5000/ or by visiting https://Salquraishi.herokuapp.com/ 

- Authentication: was set up using Auth0 jwt, at the end of the file tokens for each role are provided for reviewer testing.

## Error Handling
- Errors are returned as JSON objects.

The API will return four error types when requests fail:

- 400: bad request
- 401: unauthorized
- 403: forbidden
- 404: resource not found
- 422: unprocessable

## Endpoints

### Ators

# GET/actors
# POST/actors
# PATCH/actors/<int:id>
# DELETE/actors/<int:id>

### Movies

# GET/movies
# POST/movies
# PATCH/movies/<int:id>
# DELETE/movies/<int:id>



## Roles and permissions

- The app use Auth0 to generate jwt tokens which has permissions for each of the three roles. These roles include :

### Casting Assistant

- Can view actors and movies

- Casting Assistant Token: see \Tokens.txt
- The above token is only valid for 24 hour since the submission time

### Casting Director

- All permissions a Casting Assistant has and…
- Add or delete an actor from the database
- Modify actors or movies

- Casting Director Token: see \Tokens.txt
- The above token is only valid for 24 hour since the submission time

### Executive Producer

- All permissions a Casting Director has and…
- Add or delete a movie from the database

- Executive Producer Token: see \Tokens.txt
- The above token is only valid for 24 hour since the submission time