from functools import update_wrapper
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    #return HttpResponse('Hello there')
    return render(request, 'generator/home.html')

def password(request):
    charaters = list('abcdefghijklmnopqrstuvwxyz')
    upCase = 'not required'
    spCase = 'not required'
    NumCase = 'not required'
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        charaters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        upCase = 'required'
    if request.GET.get('special'):
        charaters.extend(list('~`!@#$%^&*()_-=+:";<,.?/'))
        spCase = 'required'
    if request.GET.get('numbers'):
        charaters.extend(list('0123456789'))
        NumCase = 'required'


    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charaters)

    return render(request, 'generator/password.html', 
        {'password': thepassword, 
        'len': length, 
        'upperCase': upCase,
        'numberCase': NumCase,
        'specialCase': spCase})