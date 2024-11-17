
## Intro

A FastAPI template with beanie, jwt

## Depedencies

- fastapi
- beanie
- PyDantic

## Features

- Registration
- Email verification
- Password reset
- JWT auth login and refresh
- User model CRUD

## Setup

```shell

python -m pip install -e .

python gen_salt.py
```

## Run

```shell

docker run -d -p 27017:27017 mongo:7

pytest

uvicorn server.main:app --reload --port 8080

```