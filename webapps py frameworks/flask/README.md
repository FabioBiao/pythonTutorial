```console
# Creating and setting virtual env
py -m venv env
. env/scripts/activate

# dependencies
pip install Flask
pip install Flask-SQLAlchemy

# on mac
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

# on windows
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
