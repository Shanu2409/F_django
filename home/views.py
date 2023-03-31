from django.shortcuts import render, HttpResponse
from datetime import datetime, date
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(req):
    context = {
        'var': "shanu"
    }

    messages.success(req,"this is test message")
    return render(req, "index.html", context) 
    #render() is used to return static or template files
    # return HttpResponse("this is index page") #HttpResponse() is used to return string


def about(req):
    return render(req, "about.html") 
    # return HttpResponse("this is about page")

def services(req):
    return render(req, "services.html") 
    # return HttpResponse("this is services page")

def contact(req):
    if req.method == "POST":
        print("inside the post")
        name = req.POST.get("name")
        email = req.POST.get("email")
        phone = req.POST.get("phone")
        description = req.POST.get("description")
        
        contact = Contact(name = name, email = email, phone = phone, description = description, date = datetime.today())
        contact.save()
        messages.success(req, "Your message has been successfuly sent.")

    return render(req, "contact.html") 
    # return HttpResponse("this is contact page")
