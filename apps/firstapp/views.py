# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from .models import User, Ideas, Like
from django.shortcuts import render, redirect
from django.db.models import Sum, Count

# Create your views here.
def index(request):
    return render(request, 'work/index.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def submit_register(request):
    goto = "/bright_ideas"
    response = User.objects.createUser(request.POST)
    #if response was successful put user info in session
    if response['status']:
        request.session['alias'] = response['user'].alias
        request.session['user_id'] = response['user'].id
        return redirect('/bright_ideas')
    #else show error messages
    else:
        for error in response['errors']:
            messages.error(request, error)
            goto = "/"
    return redirect(goto)

def logon(request):
    u = User.objects.all()
    i = Ideas.objects.all().annotate(total_likes=Sum('likes_received__total_likes'))
    t = Like.objects.all()
    context = { 'user': u, 'ideas': i, 'likes': t,
    }
    return render(request, 'work/home.html', context)
    
def submit_signin(request):
    goto = "/"
    response = User.objects.login_validation(request.POST)
    if response['status']:
        request.session['alias'] = response['user'].alias
        request.session['user_id'] = response['user'].id
        return redirect('/bright_ideas')
    else:
        for error in response['errors']:
            messages.error(request, error)
            return redirect(goto)
    return redirect(goto)

def submit_ideas(request):
    author = User.objects.get(id=request.POST['author_id'])
    user = User.objects.get(id=request.session['user_id'])
    Ideas.objects.create(text=request.POST['text'], user=user, author=author)
    return redirect('/bright_ideas')

def uprof(request, id):
    u = User.objects.get(id=id)
    c = Like.objects.aggregate(Sum('total_likes'))
    y = c.objects.filter(u)
    context = { 'user': u, 'ideas': Ideas.objects.values("text").annotate(Count("id")), 
            't': y
    }
    print context
    return render(request, 'work/userprofile.html', context)

def createLike(request):
    Like.objects.createLike(request.POST, request.session['user_id'])
    return redirect('/bright_ideas')

