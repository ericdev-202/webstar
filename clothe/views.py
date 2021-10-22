from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
	return render(request,'temps/home.html')


def fa(request):
	return render(request,'temps/faq.html')

# def book(request):
# 	return render(request,'temps/book.html')

def contact(request):
	return render(request,'temps/contacts.html')
	

def servi(request):
	return render(request,'temps/services.html')

def about(request):
	return render(request,'temps/about.html')

def team(request):
	return render(request,'temps/team.html')

def log(request):
	return render(request,'registration/login.html')

def sign(request):
	return render(request,'registration/signup.html')