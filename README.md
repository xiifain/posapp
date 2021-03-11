# Instructions for building the project
 Create a directory in a desired file location.
 ```console
 user@user:~$ mkdir <directory_name>
 user@user:~$ cd <directory_name>
 user@user:~$ touch Dockerfile docker-compose.yml
 ```

Then in the Dockerfile, copy the below code and paste into it

```Dockerfile
    FROM python:3.9-alpine

    ENV PYTHONUNBUFFERED 1

    COPY ./requirements.txt /requirements.txt

    # Install postgres client
    RUN apk add --update --no-cache postgresql-client

    # Install individual dependencies
    # so that we could avoid installing extra packages to the container
    RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
    RUN pip install -r /requirements.txt

    # Remove dependencies
    RUN apk del .tmp-build-deps

    RUN mkdir /app
    COPY ./app /app

    WORKDIR /app

    # [Security] Limit the scope of user who run the docker image
    RUN adduser -D user

    USER user
```
In docker-compose.yml file

```yaml
version: "3"

services:
  app:
    container_name: pos_app
    image: pos_app:1.0.0
    build:
      context: .
    ports:
      - "3003:3003"
    volumes:
      - ./app:/app
    command: >
      sh -c "python manage.py runserver 0.0.0.0:3003"
    environment: 
      - DB_HOST=db
      - DB_NAME=mydb-dev
      - DB_USER=admin
      - DB_PASS=password
    depends_on: 
      - db
  db:
    container_name: postgres-db
    image: postgres:13-alpine
    environment: 
      - POSTGRES_DB=mydb-dev
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=password
    ports:
      - "5432:5432"
    volumes:
      - data-volume:/var/lib/postgresql/data

volumes:
  data-volume:
```

Build the docker image with 
```console
docker-compose build
```
And run the containers with
```console
docker-compose up
```
If there are any migrations to be made
```console
```

