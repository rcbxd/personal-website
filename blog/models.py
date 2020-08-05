from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    body = models.TextField()

    def __str__(self):
        return self.title


class PostImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
