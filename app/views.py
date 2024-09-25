from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie,Wishlist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse


# Create your views here.
def index(req):
    allmovie=Movie.objects.all()
    context={"allmovie":allmovie}
    return render(req,"index.html",context)

def signup(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        context = {}

        if uname == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signup.html", context)
        elif upass != ucpass:
            context["errmsg"] = "Password and confirm password doesn't match"
            return render(req, "signup.html", context)
        else:
            try:
                userdata = User.objects.create(username=uname, password=upass)
                userdata.set_password(upass)
                userdata.save()
                return redirect("/signin")
            except:
                context["errmsg"] = "User Already exists"
                return render(req, "signup.html", context)
    else:
        context = {}
        context["errmsg"] = ""
        return render(req, "signup.html", context)


                    
                    
def signin(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        context = {}
        print(uname,upass)
        if uname == "" or upass == "":
            context["errmsg"] = "Field can't be empty!"
            return render(req, "signin.html", context)
        else:
            userdata = authenticate(username=uname, password=upass)
            if userdata is not None:
                login(req, userdata)
                return redirect("/payment_gateway1")
            else:
                context["errmsg"] = "Invalid username and password!"
                return render(req, "signin.html", context)
    else:
        return render(req, "signin.html")
    

def userlogout(req):
    logout(req)
    return redirect("/")


def payment_gateway1(req):
    return render(req,"payment_gateway1.html")

def payment_gateway2(req):
    return render(req,"payment_gateway2.html")


def mainpage(req):
    allmovie=Movie.objects.all()
    context={"allmovie":allmovie}
    return render(req,"mainpage.html",context)
    
                    
                    
def horrorlist(req):
    if req.method=="GET":
        allmovie=Movie.moviemanager.horror_list()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    else:
        allmovie=Movie.objects.all()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    
def comedylist(req):
    if req.method=="GET":
        allmovie=Movie.moviemanager.comedy_list()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    else:
        allmovie=Movie.objects.all()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    
def sciencefictionlist(req):
    if req.method=="GET":
        allmovie=Movie.moviemanager.science_fiction_list()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    else:
        allmovie=Movie.objects.all()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    
def adultlist(req):
    if req.method=="GET":
        allmovie=Movie.moviemanager.adult_list()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    else:
        allmovie=Movie.objects.all()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    
def thrillinglist(req):
    if req.method=="GET":
        allmovie=Movie.moviemanager.thrilling_list()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    else:
        allmovie=Movie.objects.all()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    
def romancelist(req):
    if req.method=="GET":
        allmovie=Movie.moviemanager.romance_list()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    else:
        allmovie=Movie.objects.all()
        context={"allmovie":allmovie}
        return render(req,"mainpage.html",context)
    

from django.contrib import messages
from django.db.models import Q


def searchmovie(req):
    query=req.GET.get("q")
    if query:
        allmovie=Movie.objects.filter(
            Q(title__icontains=query)
            |Q(category__icontains=query)
            |Q(description__icontains=query)
        )
        if len(allmovie)==0:
            messages.error(req,"No Results Found!!")
    else:
        allmovie=Movie.objects.all()

    context={"allmovie":allmovie}
    return render(req,"mainpage.html",context)
        

def wishlist(req):
    user=req.user
    allwishlist=Wishlist.objects.filter(userid=user.id)
    context={"allwishlist":allwishlist}
    return render(req,"wishlist.html",context)

def removefavourite(req,movieid):
    user=req.user
    wishitems=Wishlist.objects.get(movieid=movieid,userid=user.id)
    wishitems.delete()
    return redirect("/mainpage")

def addtofav(req,movieid):
    if req.user.is_authenticated:
        user=req.user
    else:
        user=None

    allmovie=get_object_or_404(Movie,movieid=movieid)
    wishitem,created=Wishlist.objects.get_or_create(movieid=allmovie,userid=user)
    if not created:
        wishitem.qty+=1
    else:
        wishitem.qty = 1
    wishitem.save()
    return redirect("/wishlist")
    

def video(req,movieid):
    allmovie=Movie.objects.get(movieid=movieid)
    context={"allmovie":allmovie}
    return render(req,"video.html",context)


from django.core.mail import send_mail


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        plan = request.POST.get('plan')

        


       
        send_mail(
            subject='Netflix Subscription Successful',
            message=f'Thank you for subscribing to Netflix! You chose the {plan.capitalize()} plan. ',
            from_email='sneadensiddique@gmail.com',
            recipient_list=[email],
            fail_silently=False,)

        # Redirect to a success page after subscription
        return redirect('subscription_success')
    
    # If the request is not POST, render the payment page again
    else:
        return redirect('payment_gateway2')

def subscription_success(request):
    return render(request, 'success.html')


def tvshows(req):
    return render(req,"tvshows.html")

def movies(req):
    return render(req,"movies.html")