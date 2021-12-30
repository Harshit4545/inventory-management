from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

from .models import User,books

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Book/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "Book/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Book/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "Book/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "Book/register.html")


def index(request):
    book = books.objects.all()      
    return render(request, "Book/index.html",{"book":book})

def newbook(request):
    if request.method == "POST" and request.FILES['myfile']:
        newbook = books()
        newbook.book_name =  request.POST["bookname"]
        newbook.user = request.user
        newbook.author_name = request.POST["authorname"]
        
        if request.FILES['myfile']:
         myfile = request.FILES['myfile']
         fs = FileSystemStorage()
         filename = fs.save(myfile.name, myfile)
         file = fs.url(filename)
         newbook.bookpdf = file 
        else :
         newbook.bookpdf = "NO FILE FOUND"
         
        newbook.save()
        
        return HttpResponseRedirect(reverse("index")) 
    
    return render(request,"Book/newbook.html")
   
def deletebook(request,book_id):
    dlt = books.objects.get(id=book_id)
    #dlt = books.objects.filter(id=getting)
    dlt.delete()
    return render(request,"Book/index.html")  
