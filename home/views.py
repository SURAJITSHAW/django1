from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # cotext is set of variables you want to pass into templates
    context = {
        "first_name": "Surajit",
        "last_name": "Shaw"
    }

    return render(request, 'index.html', context)
    # return HttpResponse("This is Home Page") 

def about(request):
    return HttpResponse("This is About Page")
