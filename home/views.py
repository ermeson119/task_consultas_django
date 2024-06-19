from django.shortcuts import render

    
# Create your views here.
def home(requeste):
    context = {
        'title': 'Home',
    }
    return render(requeste, "home/home.html",context)

    