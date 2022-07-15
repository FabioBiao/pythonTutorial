# create and start activate
```console
# Creating and setting virtual env
py -m venv env
. env/scripts/activate

# command to check environment
env | grep VIRTUAL_ENV

# install dependencies
pip install Flask
pip install sqlalchemy
pip install flask_sqlalchemy

```

# run code
- python server.py

# create db
- python
from server import db
db.create_all()
exit()

# generate random data
- py generate_dummy_data.py