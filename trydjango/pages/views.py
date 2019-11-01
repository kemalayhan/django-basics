from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    
    return render(request, "contact.html")

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "this is about me",
        "my_number" : 123,
        "my_list" : [323, 4235, 5343, "abc"],
        "my_html" : "<h2>My HTML</h2>"
    }
    return render(request, "about.html", my_context)