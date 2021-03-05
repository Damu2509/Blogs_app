from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

posts = [
    {
        'author' : "Damodhar reddy",
        'date_posted' : "06-mar-2021",
        'title' : "Blog Post 1",
        'content' : "This is my first blog post"
    },
    {
        'author' : "Sreenivas",
        'date_posted' : "06-mar-2021",
        'title' : 'Blog Post 2',
        'content' : "This is my second blog post"
    }
]


def home(request):
    context={
        'posts' : posts
    }
    return render(request,"blog_app/home.html",context)

def about(request):
    return render(request,"blog_app/about.html",{'title': 'About home'})