from django.shortcuts import render, HttpResponse

# Create your views here.

# Runs from urls.py -> loremaster_app.urls.py then to here.
def index(request, *args, **kwargs): #*args and ** kwargs are tuples that hold arguments that are passed to the view therefore the HTML

    return render(request, 'index.html')