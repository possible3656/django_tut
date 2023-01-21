from django.db import models

# Create your models here.


class Articles(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()


# this added to get name as a object name 
    def __str__(self):
        return self.name
