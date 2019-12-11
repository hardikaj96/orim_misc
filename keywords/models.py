from django.db import models

# Create your models here.
class Keywords(models.Model):
    keyword = models.CharField(max_length=100)

class TitlesGeneral(models.Model):
    keyword = models.CharField(max_length=100)
    date = models.TextField()
    page = models.IntegerField()
    position = models.IntegerField()
    title = models.TextField()
    author = models.TextField()
    publisher = models.TextField()
    pages = models.FloatField()
    publication_date = models.CharField(max_length=100)
    sales_rank = models.FloatField()
    image = models.CharField(max_length=100)
    asin = models.CharField(max_length=100)