# alc
ALCDevops Challenge

## Prerequisites

* Docker
* Python 2.7
* Terminal

Install docker community edition from this link https://www.docker.com/community-edition  
This code has only been tested on a macOS computer.  
  
  
Test docker installation by typing this command into terminal  
```
$ docker -v
```  
  
You should get an output similar to this:  
```
Docker version 17.12.0-ce, build c97c6d6
```


### Deployment
clone this repo with this  
```
$ git clone https://github.com/abduladi/alc.git
```  

Navigate into the the clone folder with  
```
$ cd alc  
```  

Run the `dockapp.py` file with this  
```
$ python dockapp.py
```  

### Execution

Api can be accessed as provided by repository that developed the application  
https://github.com/BolajiOlajide/UserManager  

### API Documentation
The API only has one endpoint which is the `/users` endpoint for saving users to the database. The endpoint works with the HTTP verbs: `POST`, `GET`, `PUT`, `DELETE`.

###### POST HTTP Request
-   `POST` /users
-   INPUT:
```x-form-url-encoded
name: John Doe
email: john.doe@gmail.com
password: johndoe
```

###### HTTP Response

-   HTTP Status: `201: created`
-   JSON data
```json
{
  "_id": "59071791b0lkscm2325794",
  "name": "John Doe",
  "email": "john.doe@gmail.com",
  "password": "johndoe",
  "__v": 0
}
```

###### GET HTTP Response
-   `GET` /users

```json
[
    {
        "_id": "59071791b0lkscm2325794",
        "name": "John Doe",
        "email": "john.doe@gmail.com",
        "password": "johndoe",
        "__v": 0
    }
]
```

###### GET HTTP Response
-   `GET` /users/:id

```json
{
    "_id": "59071791b0lkscm2325794",
    "name": "John Doe",
    "email": "john.doe@gmail.com",
    "password": "johndoe",
    "__v": 0
}
```

###### DELETE HTTP Response
-   `DELETE` /users/:id

```json
User John Doe was deleted
```

###### POST HTTP Request
-   `PUT` /users/:id
-   INPUT:
```x-form-url-encoded
name: Jane Doe
email: jane.doe@gmail.com
password: janedoe
```

###### HTTP Response

-   HTTP Status: `200: OK`
-   JSON data
```json
{
  "_id": "59071791b0lkscm2325794",
  "name": "Jane Doe",
  "email": "jane.doe@gmail.com",
  "password": "janedoe",
  "__v": 0
}
```


