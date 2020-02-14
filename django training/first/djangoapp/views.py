from django.shortcuts import render,redirect
from django.http import HttpResponse
from djangoapp.models import posts,UserData
from djangoapp.form import  UserForm, RegForm, post_form
import csv
from reportlab.pdfgen import canvas
from django.core.mail import send_mail
from first import settings
# from djangoapp.functions import handle_upload_file

from datetime import datetime 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

bstrap = '''
			<html>
			<head>
			<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
			</head>
			<body>
			<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
			<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
			<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

		 '''
# Create your views here.
def index(request):
    return HttpResponse("<h1>sht</h1>")

def custom_reg(request):
	if request.method == 'POST':
		user = UserForm(request.POST)
		form = RegForm(request.POST)
		if user.is_valid() and form.is_valid():
			profile = form.save(commit= 0)
			profile.user = request.user 
			user.save()
			profile.save()
			return redirect('/login/')

	else:
		user= UserForm()
		form = RegForm()
	return render(request, "registration/customreg.html", {'form':form, 'user':user})


def check(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username = username, password = password)
	if user is not None:
		login(request,user)
		return redirect('/home')
	else: return redirect('/login')


#--------------------------------------------------------
from random import shuffle
@login_required
def home(request):
	un = request.user.username
	data=[]
	try:
		dat = posts.objects.all()
		for d in dat:
			if d.user!=un:
				data.append(d)

	except: pass
	shuffle(data)
	if len(data)>10:
		data = data[:10] 
	return render(request, 'home.html',{'username':un,'opost':data})

def logoutpage(request):
	logout(request)
	return redirect('/login')

@login_required
def makepost(request):

	if request.method=='POST':
		form = post_form(request.POST)
		if form.is_valid():
			# post = request.POST['post']
			# author = request.user.username
			# date = str(datetime.now())
			post = posts()
			post.head = request.POST['head']
			post.post =  request.POST['post']
			post.user = request.user.username
			post.date = str(datetime.now())
			post.save()
			return redirect('/home/')
	else:
		form = post_form()
	return render(request,'makepost.html',{'form':form,'username':request.user.username})

@login_required
def postpage(request):
	user = request.user.username
	data=[]
	try:
		data = posts.objects.all().filter(user=user)
	except: pass

	return render(request,'postpage.html',{'posts':data,'username':user})

@login_required
def deletepost(request,id):
	
	try:
		std = posts.objects.get(id=id)
		std.delete()
	except: pass
	return redirect("/posts/")

@login_required
def copypost(request,id):
	try:
		post = posts()
		std = posts.objects.get(id=id)
		post.head = std.head
		post.post =  std.post 
		post.user = request.user.username
		post.date = std.date + " -----copied from: "+std.user + "-------"
		post.save()
	except: pass
	return redirect("/home/")

def homepage(request):
	data=[]
	try:
		for d in posts.objects.all():
			data.append(d)
			shuffle(data)
	except: pass
	
	if len(data)>10:
		data = data[:10] 
	return render(request,'index.html',{'title':'django training','opost':data})