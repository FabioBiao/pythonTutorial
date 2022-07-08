# Commands
- run server: 
python manage.py runserver

- create app: 
python manage.py startapp polls

- migrate DB: 
python manage.py migrate
- migrate polls BD: 
python manage.py makemigrations polls
## sqlmigrate command takes migration names and returns their SQL
- python manage.py sqlmigrate polls 0001

## making model changes
- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.

## set env
- .\env\Scripts\activate

# create admin user
- python manage.py createsuperuser

## access admin page
- http://127.0.0.1:8000/admin/


## to add the polls to the admin, go to admin.py and add the models there

# running tests
- python manage.py test polls

## running tests on shell  - https://docs.djangoproject.com/en/4.0/intro/tutorial05/
- python manage.py shell
- >>> from django.test.utils import setup_test_environment
- >>> setup_test_environment()


# finding admin templates
- python -c "import django; print(django.__path__)"
after that go to django/contrib/admin/templates and copy the templates, to your template folder, you need to set it's path on th settings.