## requirements
Python3
Pip3

## Commands
``pip3 install -r requirements.txt``
``source env/bin/activate``
``flask run``

## Basic commands

Show all dependencies
```
docker-compose exec web pip freeze
```

Install new dependecie
```
docker-compose exec web pip install {dependencie_name}
```

for run flask instruction
<br>
```
docker exec -i -t python-web /bin/bash
```
<br>

```
 $ flask {instruction}
```


Another way to run commands
<br>

```
docker-compose exec web flask {command}
```

## Database connection

For in into database

```
docker-compose exec db psql -U postgres
```

Running migrations
```
docker-compose exec web flask db init
docker-compose exec web flask db stamp head
docker-compose exec web flask db migrate
docker-compose exec web flask db upgrade
```



