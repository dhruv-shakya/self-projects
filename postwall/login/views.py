from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['phone_num']
        paswd = request.POST['pswd']

        user = auth.authenticate(username=username, password=paswd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/login/')
    else:
        return render(request, 'login.html')
        

def register(request):
    if request.method == 'POST':
        username = request.POST['phone_num_reg']     # username is phone no.
        fullname = request.POST['fullname']
        passwd = request.POST['pswd_reg']
        passwd1 = request.POST['pswd_reg2']

        context = {'fullname':fullname, 'username':username}

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return render(request, 'login.html', context)
        elif len(username) != 10:
            messages.info(request, 'Invalid Mobile Number')
            return render(request, 'login.html', context)
        elif passwd != passwd1:
            messages.info(request, 'password not match')
            return render(request, 'login.html', context)
        else:
            user = User.objects.create_user(username=username,first_name=fullname ,password=passwd)
            user.save()
            auth.login(request,user)
            return redirect('/')
    else:
        return redirect('/login/')

def logout(request):
    auth.logout(request)
    return redirect('/')
