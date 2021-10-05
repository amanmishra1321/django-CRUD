from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import User


@api_view(['POST','GET'])
@csrf_exempt 
def signin(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = authenticate(request,email=email,password=password)
        print(user)
        if user:
            login(request,user)
            return Response("Login Successful")
        return Response("Email or Password is invalid")
    return Response("Get method is not allowed")


@api_view(['POST','GET'])
@csrf_exempt
def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        phoneno = request.POST['phoneno']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        try:
            user = User(email=email,phoneno=phoneno,first_name=first_name,last_name=last_name)
            user.set_password(password)
            user.save()
            return Response("Response Created")

        except:
            return Response("Email or Phone number exists")