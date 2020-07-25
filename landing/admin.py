from django.contrib import admin

from .models import Category, Skill, SubSkill

admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(SubSkill)
