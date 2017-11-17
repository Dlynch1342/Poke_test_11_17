from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User
import bcrypt

def index(request):
	return render(request, 'login/main.html')

def register(request):
	
	result = User.objects.register(request.POST)

	if 'err_messages' in result:
		for e in result['err_messages']:
			messages.error(request, e)

	else:
		request.session['id'] = result['success'].id
		return redirect('/success')

	
	return redirect('/')

def login(request):
	return redirect('/success')

def success(request):
	context = {
		"user": User.objects.get(id=request.session['id'])
		

	}
	route = 'poke_app:home'

def logout(request):
	try:
		request.session.clear()
	except:
		pass
	return redirect('/')
	
