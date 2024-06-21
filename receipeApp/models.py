from django.db import models

# Create your models here.
class recipes(models.Model):
    Name = models.CharField(max_length = 100)
    Time = models.IntegerField()
    steps = models.TextField()
    image = models.CharField(max_length=500)
