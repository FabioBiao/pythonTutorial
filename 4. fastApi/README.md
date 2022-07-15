# create and start activate
```console
# Creating and setting virtual env
py -m venv env
. env/scripts/activate


# install dependencies
pip install fastapi
pip install "uvicorn[standard]"
```

# run code
- uvicorn main:app --reload

# create db

ASGI documentation - server


# to manage database we are using pydantic
- https://pydantic-docs.helpmanual.io/


# swagger integrated on fast API 
## we can test APIs on this swagger
- http://127.0.0.1:8000/docs

# we also get redoc
http://127.0.0.1:8000/redoc