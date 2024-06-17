from django.shortcuts import render

# Create your views here.

def setup(requeste):
    return render(requeste, "setup/index.html")