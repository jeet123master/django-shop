from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

@login_required(login_url="login")
def Dashboard(request):
	return render(request, 'frontpage/dashboard.html')

def UserRegister(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = CreateUserForm

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account created successfully for ' + user)
				return redirect('login')
			else:
				messages.error(request, 'error')
		context = {
			'form' : form
		}
		return render(request, 'frontpage/register.html', context)

def UserLogin(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.error(request, 'Username or password is incorrect')
				return render(request, 'frontpage/login.html')

		return render(request, 'frontpage/login.html')

def UserLogout(request):
	logout(request)
	return redirect('login')