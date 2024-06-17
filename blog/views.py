from django.shortcuts import render

# Create your views here.
def blog(requeste):
    return render(requeste, "blog/blog.html")