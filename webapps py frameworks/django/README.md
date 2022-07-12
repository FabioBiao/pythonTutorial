## Steps:

```console
# Creating and setting virtual env
py -m venv env
. env/scripts/activate
```

### Installation

```console
pip install Django
# this creates the django project with the name todoapp
django-admin startproject todoapp
```

### Start

```console
python manage.py migrate
python manage.py runserver
# command bellow generates a app "todolist"
python manage.py startapp todolist
```

- add 'todolist' to INSTALLED_APPS inside the todoapp/settings.py file

### Add views
- implement todolist.views.py and create todolist.urls.py
- add urls to todoapp.urls.py

### Add templates
- add templates folder and file
- add "templates" to DIR in todoapp/settings.py
- modify view: return render...

### Add models
- implement todolist.models.py

### Put together
```console
python manage.py makemigrations todolist
manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

- Adding models to the administration site:
    - todolist.admin.py: admin.site.register(Todo)
- login to admin

### add template
- add {% csrf_token %} to template

### CRUD
- implement views