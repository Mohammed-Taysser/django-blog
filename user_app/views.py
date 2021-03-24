from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoinForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_user(request):
	if request.method == 'POST':
		user_form = LoinForm()
		user_auth = authenticate(request, username=request.POST['username'], password = request.POST['password'])
		if user_auth is not None:
			login(request, user_auth)
			return redirect('home')
		else:
			messages.warning(request, 'user name or password is Wrong')
	else:
		user_form = LoinForm()
	data = {
		'page_name': 'Login',
		'user_form': user_form,
	}
	return render(request, 'user_app/login.html', data)


def logout_user(request):
	return render(request, 'user_app/logout.html')


def profile(request):
	return render(request, 'user_app/profile.html')


def update_profile(request):
	return render(request, 'user_app/update_profile.html')


def register_user(request):
	if request.method == 'POST':
		user_form = UserCreationForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			messages.success(request, f'congratulation {user_form.cleaned_data["username"]} registration had been successfully')
			return redirect('home')
	else:
		user_form = UserCreationForm()
	data = {
		'page_name': 'register'.title(),
		'user_form': user_form,
	}
	return render(request, 'user_app/register.html', data)
