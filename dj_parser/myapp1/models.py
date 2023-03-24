from django.db import models

# Create your models here.
class Parsing(models.Model):
    title = models.CharField(max_length=63, blank=False)
    link = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return f'T :: {self.title}'