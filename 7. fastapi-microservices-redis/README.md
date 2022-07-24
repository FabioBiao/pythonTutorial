# create redis DB on
- https://redis.io/
- configurations of this on this repo, no longer exists. You need to create one redis DB yourself. 

# create and start activate
```console
# Creating and setting virtual env
py -m venv env
# activate
. env/scripts/activate
# deactivate

# upgrate packages
py -m pip install --upgrade SomeProject

# using virtualenv, to set specific python version
virtualenv -p python3.9 env

# install dependencies
pip install -r requirements.txt

```

# Create requirements
```console
pip3 freeze > requirements.txt  # Python3
pip freeze > requirements.txt  # Python2
```
