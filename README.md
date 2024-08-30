# YourHero - StarWars
## An API built with Django DRF to list / search / sort StarWars Characters

* `Public` endpoint to `list, search, and order` the results of StarWars Characters.  

* `Private` endpoint for `Users` to `list and add` Characters to their favorites with JWT authentication available in production mode.  
_In development mode for convenience you can employ BasicAuth to test authenticated routes. A local SQLite DB will be created if DATABASE_URL is not defined. Development mode runs on `:8002` port._  

**Live Demo**: Hosted in a DigitalOcean VM with a cloud Postgres instance in aiven.io.  
Available on: `https://starwars.jbin.me/api/`  
  
  
Live Demo Example:
```shell
https://starwars.jbin.me/api/people/?planet=Tatooine&ordering=-mass
```  

## Available APIs
* #### All Starwars Characters: [GET] `people/`
_Development_
```shell
 curl http://127.0.0.1:8002/api/people/
```  
_**Live Demo**_
```shell
curl https://starwars.jbin.me/api/people/
```
___
### Search and Order

* #### Search by name: [GET] `people/?name={name}`
_Development_
```shell
 curl http://127.0.0.1:8002/api/people/?name=Luke
```  
_Live Demo_
```shell
curl https://starwars.jbin.me/api/people/?name=Luke
```
___
* #### Search by planet: [GET] `people/?planet={planet}`
_Development_
```shell
 curl http://127.0.0.1:8002/api/people/?planet=Tatooine
```  
_Live Demo_
```shell
curl https://starwars.jbin.me/api/people/?planet=Tatooine
```
___
* #### Order by: [GET] `people/?ordering={- (for DESC)}{name | mass | height | birth_year}`
_Development_
```shell
 curl http://127.0.0.1:8002/api/people/?ordering=-name
```  
_Live Demo_
```shell
curl https://starwars.jbin.me/api/people/?ordering=-name
```
___


## User Endpoints  
* #### Create USER: [POST] `auth/users`
    Request data arguments:  
        {
            "username": "xxxx",
            "password": "xxxxxx",
            "email": "xxxx@xxxx.com"
        }  

_Development_
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "user2", 
        "password": "user2password",
        "email": "user2@user2.com"}' \
  http://127.0.0.1:8002/api/auth/users/
```  
_Live Demo_
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "user2", 
        "password": "user2password",
        "email": "user2@user2.com"}' \
  https://starwars.jbin.me/api/auth/users/
```
___
___
* #### Access Token in Production mode: [POST] `auth/token/`
    Request data arguments:  
        {
            "username": "xxxx",
            "password": "xxxxxx"
        }  

_Live Demo_
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "user2", "password": "user2password"}' \
  https://starwars.jbin.me/api/auth/token/
```
______
* #### USER add Characters to favorites: [POST] `people/favorites/`
    Request data arguments :  
    List of Character IDs:     `{
            [id1, id2, ...]
        }  `
 

_Development_
```shell
curl \
  -X POST \
  -u user2:user2password \
  -H "Content-Type: application/json" \
  -d '[1, 2, 3]' \
  http://127.0.0.1:8002/api/people/favorites/
```  
_Live Demo_
```shell
curl \
  -X POST \
  -H "Authorization: Bearer {acccess token}" \
  -H "Content-Type: application/json" \
  -d '[1, 2, 3]' \
  https://starwars.jbin.me/api/people/favorites/
```
___
* #### USER views favorite Characters: [GET] `people/favorites/`

_Development_
```shell
curl \
  -u user2:user2password \
  http://127.0.0.1:8002/api/people/favorites/
```  
_Live Demo_
```shell
curl \
    -H "Authorization: Bearer {acccess token}" \
  https://starwars.jbin.me/api/people/favorites/
```
___

## Development Mode
#### Create a python virtual environment and activate it:

```shell
python3 -m venv env
source env/bin/activate
```

#### Install dependancies from the `requirements.txt`:

```shell
pip install -r requirements.txt
```
### Usage
#### Populate the DB  
You need to run `load_people` manage.py command after migrate. This needs to run one time to fetch the data from swapi.dev and populate the database.
```shell
python manage.py migrate
python manage.py load_people
```  
#### Add a .env file in root directory with 
```shell
DEBUG=True
```  
#### Run development server
```shell
python manage.py runserver
```  