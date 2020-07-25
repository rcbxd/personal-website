from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Skill(models.Model):
    technology = models.CharField(max_length=200)
    time_learned = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class SubSkill(models.Model):
    technology = models.CharField(max_length=200)
    time_learned = models.DateTimeField(auto_now=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
