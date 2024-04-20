from django.db import models

#Object relation Mapping - Django Migrations
# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default=False)
