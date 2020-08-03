from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost
#from .models import BlogImage


def blog(request):
    # get all of the posts
    return render(request, "blog/index.html", locals())


def blog_post(request, post_id):
    # get the post details
    post = get_object_or_404(BlogPost, pk=post_id)
    # get the post images
    return render(request, "blog/blog_post.html", locals())
