from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost, PostImage
#from .models import BlogImage


def blog(request):
    # get all of the posts
    posts = BlogPost.objects.all()
    return render(request, "blog/index.html", locals())


def blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    post_images = PostImage.objects.filter(post=post)
    print(post_images)
    return render(request, "blog/blog_post.html", locals())
