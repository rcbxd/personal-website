from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    body = models.TextField()
