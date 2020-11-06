from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateTimeField()
    body = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images/')
