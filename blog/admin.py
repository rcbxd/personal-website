from django.contrib import admin
from .models import BlogPost, PostImage

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(PostImage)
