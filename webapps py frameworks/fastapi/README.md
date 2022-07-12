```console
# Creating and setting virtual env
py -m venv env
. env/scripts/activate

# installing dependencies
pip install fastapi
pip install "uvicorn[standard]"
pip install python-multipart sqlalchemy jinja2

# run fastAPI with hot reload
uvicorn app:app --reload

# also API swager documentation on
http://127.0.0.1:8000/docs
```

# Uvicorn
Is a low-level server/application interface for async frameworks
- https://www.uvicorn.org/deployment/

