# ClassRoom App

#### Project Structure :
```
classroom-docker/
    screenshots/
    classroom/
        classroom/
        classroomapp/
        templates/
        db.sqlite3
        manage.py
    entrypoint.sh
    requirements.txt
    Dockerfile
    docker-compose.yml
    README.md
```

## Getting Started

#### Using Docker

Get in the Project Folder

```sh
$ cd classroom-app
$ sudo docker-compose up --build
```

#### Installing in own system

Create a Virtual environment and activate it
```sh
$ cd classroom-app
$ virtualenv -p /usr/bin/python3 newenv
$ source newenv/bin/activate
```

```sh
$ pip install -r requirements.txt
$ python classroom/manage.py makemigrations classroomapp
$ python classroom/manage.py migrate
$ python classroom/manage.py runserver 8080
```

### Use
    - Server can be accessed at http://localhost:8080/
    - Admin Panel can be accessed at http://localhost:8080/admin/
    - Creds - username=admin password=admin
    - Dummy data can be found in `db.sqlite3`
    - Each problem can be accessed via the list in the index page

## Stack Info

  * **Python 3.7**
  * **Django 3.0**
