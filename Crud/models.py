from django.db import models

# Create your models here.
class Bookes(models.Model):
    name = models.CharField(max_length=200)
    Author = models.CharField(max_length = 35)
    Price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'Bookes'