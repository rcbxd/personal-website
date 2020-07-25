from django.db import models


class Master(models.Model):
    nickname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    picture = models.ImageField(max_length=200)

    instagram_link = models.CharField(max_length=200)
    soundcloud_link = models.CharField(max_length=200)
    telegram_link = models.CharField(max_length=200)
    twitter_link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)

    def __str__(self):
        return self.nickname


class Category(models.Model):
    name = models.CharField(max_length=200)
    has_subcategory = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    has_skill = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category.name} -> {self.name}"


class Skill(models.Model):
    technology = models.CharField(max_length=200)
    time_learned = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    has_subskill = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category} -> {self.technology}"


class SubSkill(models.Model):
    technology = models.CharField(max_length=200)
    time_learned = models.DateTimeField(auto_now=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.skill} -> {self.technology}"
