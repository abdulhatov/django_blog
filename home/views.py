from django.shortcuts import render, redirect, HttpResponse
from .models import (
    Blog,
    Area,
)

from .forms import (
    CreateBlog,
    UpdateBlog,
)

def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, "home/blogs.html", context)

def create_blog(request):

    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Blog.objects.create(
            title = title,
            body = body,
        )
        return redirect('http://localhost:8000/')

    form = CreateBlog()
    context = {
        'form':form
    }
    return render(request, "home/create_form.html", context)


def update_blog(request, id):
    blog = Blog.objects.get(pk=id)

    if request.method == 'POST':
        blog = UpdateBlog(request.POST, instance=blog)
        if blog.is_valid():
            blog.save()
            return redirect('http://localhost:8000/')
        return HttpResponse("Invalid !")
    update_blog_form = UpdateBlog(instance=blog)
    context = {
        'update_blog_form': update_blog_form
    }
    return render(request, "home/update_blog.html", context)


def delete_blog(request, id):
    try:
        blog = Blog.objects.get(pk=id)
        blog.delete()
    except:
        return HttpResponse("Маалымат табылган жок")
    return redirect('http://localhost:8000/')


def area_show(request):
    areas = Area.objects.all()
    context = {
        'areas':areas
    }
    return render(request, "home/area.html", context)


