from django.db import models

# Create your models here.
class store(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    isbn = models.IntegerField()
    price = models.IntegerField()
