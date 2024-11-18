
## Intro

A FastAPI template with beanie, jwt

## Depedencies

- fastapi
- beanie - mongo ODM (object-document mapper)
- Pydantic - validation
- JWT - authentication

## Features

- Registration
- Email verification
- Password reset
- JWT auth login and refresh
- User model CRUD

## Setup

```shell

# install and activate environment
# for venv
. .venv/bin/activate
python -m pip install -e .

# for pyenv/poetry
poetry use 3.9
poetry install

# gen encryption salt
python gen_salt.py
```

## Run

```shell

# Start mongod container
docker run -d -p 27017:27017 mongo:7

pytest

uvicorn server.main:app --reload --port 8080

```

## For VSCode debug

- Select intepretor, choose python in the environment
- This is also needed for intellesense to work.
- Press F5 to start debug, Choose Python > FastAPI
- For debug command, input `server.main:app`
