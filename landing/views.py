from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Master, Category, SubCategory, Skill, SubSkill


def index(request):
    master = get_object_or_404(Master, pk=1)
    return render(request, "landing/index.html", locals())


def about(request):
    return render(request, "landing/about.html")


def skills(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    skills = Skill.objects.all()
    subskills = SubSkill.objects.all()
    return render(request, "landing/skills.html", locals())


def projects(request):
    return render(request, "landing/projects.html")
