from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateTimeField()
    body = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:130]

    def date_pretty(self):
        return self.date.strftime('%d/%m/%Y')

    def __str__(self):
        return self.title
