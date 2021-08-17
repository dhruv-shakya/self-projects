import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime  import datetime 


def dashboard(request):
	login = request.user.is_authenticated
	post_form = Post_form()
	allpost = Post.objects.all().order_by('-id')

	context = {'login':login, 'post_form':post_form, 'allpost':allpost}
	return render(request, 'dashboard.html',context)

def update_post(request):
    if request.method == 'POST' and request.user.is_authenticated: 
        content = request.POST['content']
        form = Post_form(request.POST, request.FILES) 
        if form.is_valid(): 
            temp = form.save(commit=False) 
            temp.owner = request.user
            temp.content = content
            temp.save()
        else:
            messages.info(request, 'The maximum file size that can be uploaded is 5MB')
    else: 
        form = Post_form()
    return redirect('/')


def addlike(request):
    if request.method == 'POST' and request.user.is_authenticated: 
        post_id = request.POST['post_id_name']
        user_id = str(request.user.id)
        the_Post = Post.objects.filter(id=post_id)
        if len(the_Post)!=0:
            the_Post = the_Post[0]
            x = 1 - the_Post.likes.get(user_id, 0) 
            #  x  = 1 if  like else 0
            the_Post.likes[user_id] = x
            the_Post.num_like += (2*x-1) 
            the_Post.save()

    return redirect('/')


def addcomment(request):
    if request.method == 'POST' and request.user.is_authenticated: 
        post_id = request.POST['post_id_name'] 
        comment_val = request.POST['comment_name'] 
        user_name = request.user.first_name
        the_Post = Post.objects.filter(id=post_id)

        if len(the_Post)!=0:
            the_Post = the_Post[0]
            the_Post.comments[len(the_Post.comments)] = { 
            'user_name' : user_name, 
            'time': datetime.now().strftime("%I:%M %p %b %d, %Y"),
            'val': comment_val}
            the_Post.save()

    return redirect('/')


def deletepost(request, post_id):
    if request.user.is_authenticated: 
        Post.objects.filter(id=post_id, owner= request.user).delete()
    return redirect('/')
