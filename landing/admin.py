from django.contrib import admin

from .models import Category, SubCategory, Skill, SubSkill, Master

admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(SubSkill)
admin.site.register(Master)
admin.site.register(SubCategory)
