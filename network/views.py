from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from datetime import datetime
from .models import *
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json 
import string

#ERROR ALERT THIS PROGRAM DOES NOT ACCEPT SOME STUFF AS POSTS LIKE
#IT DOES NOT ACCEPT ANY ' THESE KIND OF MARKS AS OF NOW .


@login_required(login_url='/login')
def index(request):
    if request.method == "POST":

        # Getting the user & post 
        user = request.user 
        post = request.POST.get("input_value")

        # Making the post
        temp = posts.objects.create(user=user,post=post)

        # Redirecting to homepage 
        return HttpResponseRedirect(reverse("index"))

    else:
        post = posts.objects.all().order_by('-timestamp')
        paginator = Paginator(post, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        try:
            user=request.user 
            edit = posts.objects.filter(user=user)
        except:
            edit = ''

        return render(request, "network/index.html",{
            "posts":page_obj,
            "edit":edit,
            "c_user":request.user
        })

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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



@login_required(login_url='/login')
def profile(request,username):
    if request.method == "POST":
        user = request.user 
        username_id = User.objects.get(username=username)

        try:
            follow = request.POST.get('follow')
            unfollow = request.POST.get('unfollow')
        except:
            pass

        if follow is not None :
            try:
              q= followings.objects.get(user=user)
              
            except :
                q = followings.objects.create(user=user)

            q.following.add(username_id.id)
            q.save()
        if unfollow is not None :
            w = followings.objects.get(user=user,following=username_id.id)
            w.following.remove(username_id.id)
            w.save()

        return HttpResponseRedirect(reverse('profile',args=[username]))

    else :
        user = User.objects.get(username=username)
        current_user = request.user 

        profile_follow =''
        profile_unfollow = ''

        if user != current_user :
            try:
                followings.objects.get(user=current_user,following=user.id)
                profile_follow =''
                profile_unfollow = 'show'
            except:
                profile_follow ='show'
                profile_unfollow =''
        
        post = posts.objects.filter(user=user.id).order_by('-timestamp')
        paginator = Paginator(post, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)



        return render(request,"network/profile.html",{
            "following_count":followings.objects.filter(user=user.id).count(),
            "follower_count":user.followers.count(),
            "posts":page_obj,
            "profile_follow":profile_follow,
            "profile_unfollow":profile_unfollow,
            "username":username,
            "error":"This user has no posts"
        })

@login_required(login_url='/login')
def following(request):
    user = request.user
    post = ''
    for x in followings.objects.filter(user=user):
        for y in x.following.all():
            post = posts.objects.filter(user=y).order_by('-timestamp')
    
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"network/following.html",{
        "posts":page_obj,
        "error":"You are not following anyone"
    })

def user_request(request):
    user = str(request.user)
    return JsonResponse({"user":user})

@csrf_exempt
@login_required(login_url='/login')
def edit(request):
    if request.method == "POST":
        data = json.loads(request.body)
        posting = data.get("post","")
        user = data.get("user","")
        index = data.get("index","")

        p = posts.objects.get(user=request.user,post=index)
        p.post = posting 
        p.save()

        return JsonResponse({"message": "Post edited successfully"}, status=201)

@csrf_exempt
@login_required(login_url='/login')
def likes(request,post):

    if request.method == "POST":
        current_user = request.user
        data = json.loads(request.body)
        likes = data.get("likes","")
        clicks = data.get("clicked","")

        try:
            p = posts.objects.get(liked=current_user,post=post)
            c = click.objects.get(user=current_user,post_clicked=p.id)
            p.liked.remove(current_user)
            p.save()
            p.likes = p.likes - 1 
            p.save()
            c.icon_clicked = clicks
            c.post_clicked.remove(p.id)
            c.save()
        except:
            p = posts.objects.get(post=post)
            c = click.objects.get(user=current_user,post_clicked=p.id)
            p.liked.add(current_user)
            p.save()
            p.likes = p.likes + 1 
            p.save()
            c.icon_clicked = clicks
            c.post_clicked.add(p.id)
            c.save()

        return JsonResponse({"message": "Post edited successfully"}, status=201)

    else :
        current_user = request.user
        try :
          n = posts.objects.get(post=post)
          likes = n.likes
        except:
            likes = 0 

        try:
            p = posts.objects.get(post=post)
            c = click.objects.get(user=current_user,post_clicked=p.id) 
        except:
            p = posts.objects.get(post=post)
            c = click.objects.create(user=current_user)
            c.post_clicked.add(p.id)
            c.save()  

        clicking = c.icon_clicked
        return JsonResponse({"post_likes":likes,"clicking":clicking})
        


