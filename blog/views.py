from django.shortcuts import render

# Create your views here.
def blog(requeste):
    context = {
        'title': 'Blog',
    }
    return render(requeste, "blog/blog.html", context)