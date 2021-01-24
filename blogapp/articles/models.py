from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)