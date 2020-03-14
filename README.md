# Movie Agency

    This is a project for Udacity Fullstack Nanodegree. This web app deals with managing a film agency.
    Backend is hosted on https://hariv-capstone.herokuapp.com/


## Quick start

1. Clone it
1. `set FLASK_APP=app`
1. `flask run`

## Requirements

-   Python 3
-   Please read the [requirements file](./requirements.txt) file for more information and run the following command:
 -   `pip install -r requirements.txt`
-   If you do not have `pip`, please install it by running the following commands:
 -   `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
 -   `python get-pip.py`


## Developed with

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [SQLAlchemy](http://www.sqlalchemy.org/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Auth0](https://www.auth0.com)

## Project Setup

### Auth0 setup

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:actors`
    - `post:actors`
    - `patch:actors`
    - `delete:actors`
    - `get:movies`
    - `post:movies`
    - `patch:movies`
    - `delete:movies`
6. Create new roles for:
    - Casting Assistant
        - can   - `get:actors`
                - `get:movies`
    - Casting Director
        - can   - `get:actors`
                - `post:actors`
                - `patch:actors`
                - `delete:actors`
                - `get:movies`
                - `patch:movies`
    - Executive Producer
        - can   - `get:actors`
                - `get:movies`
                - `post:movies`
                - `delete:movies`
    - Register 3 users and assign them the three roles 
            User 1 - Casting Assistant
            User 2 - Casting Director
            User 3 - Executive Producer
    - Sign into each account and make note of the JWT.

## Endpoints
```
    localhost:5000
    heroku: https://hariv-capstone.herokuapp.com/
```
### POST '/actors'

- Adds a new actor
- Authorization required: Casting Director
- Request Arguments: Actors body

```
- Actors body: 

{
    "name": "Brad Pitt",
    "age": "56",
    "gender": "Male"
}
```
- Returns: 

```json5
{
    "actors": [
        {
            "age": "16",
            "gender": "Male",
            "id": 56,
            "name": "Brad Pitt"
        }
    ],
    "success": true
}
```
### GET '/actors'

- Fetches a dictionary of all actors
- Authorisation required: Casting Assistant/Casting Director/Executive Producer
- Returns: 

```json5
{
    "actors": [
        {
            "age": "65",
            "gender": "Male",
            "id": 2,
            "name": "Brad"
        },
        {
            "age": "65",
            "gender": "Male",
            "id": 1,
            "name": "Jim Carrey"
        }
    ],
    "success": true
}
```

### DELETE '/actors/<id>'

- Deletes an actor
- Authorization required: Casting Director
- Returns: 

```json5
{
    "deleted": 2,
    "success": true
}
```

### PATCH '/actors/<id>'

- update actors name
- Authorization required: Casting Director
- Request Arguments: Actors body

```
- Actors body: 

```json5
{
    "name": "Brad Pitt Jr",
    "age": "56",
    "gender": "Male"
}
```
- Returns: 

```json5
{
    "actors": [
        {
            "age": "16",
            "gender": "Male",
            "id": 56,
            "name": "Brad Pitt Jr"
        }
    ],
    "success": true
}
```
### POST '/movies'

- Adds a new movies
- Authorization required: Executive Producer
- Request Arguments: movies body

```json
{
    "title": "Bunny club",
    "release_date": "feb2020"
}
```
- Returns: 

```json5
{
    "movie": [
        {
            "id": 14,
            "release_date": "feb2020",
            "title": "Bunny club"
        }
    ],
    "success": true
}
```
### DELETE '/movie/1'

- Deletes a movies
- Authorization required: Executive Producer
- Returns: 

```json5
{
    "deleted": 2,
    "success": true
}
```
### Not found  (404)

```json5
{
  'success': false,
  'error': 404,
  'message': 'Resource Not Found'
}
```

### Unprocessable request (422)

```json5
{
  'success': false,
  'error': 422,
  'message': 'Unable to process request'
}
```
### Duplicate (409)

```json5
{
  'success': false,
  'error': 409,
  'message': 'Duplicate found'
}

### Internal server error (500)

```json5
{
  'success': false,
  'error': 500,
  'message': 'Internal server error'
}
```