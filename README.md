# music rec 
[![Python](https://github.com/jalbertsr/logo-badge-images/blob/master/img/rsz_python.png?raw=true)](https://www.python.org/)
[![Flask](https://github.com/jalbertsr/logo-badge-images/blob/master/img/rsz_flask.png?raw=true)](http://flask.pocoo.org/)
[![Docker](https://i.imgur.com/VyjCJuz.png)](https://www.docker.com/)

A web application to collect 5 songs from the user and return a song reccomendation in a random language.
The reccomendation is generated using OPENAI api: user name, songs, and rec uploadted to sqlite db. 
```
To run: 
Add a .env file in format: OPENAI_API_KEY =
    docker-compose build 
    docker-compose up
```



