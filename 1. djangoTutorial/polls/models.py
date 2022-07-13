from django.db import models

# Create your models here.
## need to activate models on myDjangoSite/settings.py inside the INSTALLED_APPS
##
## python manage.py makemigrations polls
## python manage.py sqlmigrate polls 0001 (this shows the queries)
## python manage.py migrate  
## 
## python manage.py shell - to test commands  - https://docs.djangoproject.com/en/4.0/intro/tutorial02/

import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    @admin.display( # this makes it show with red/green instead of true and false
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()  # fixing the bug, found on test
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


