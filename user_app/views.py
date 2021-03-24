from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoinForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog_app import models
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_user(request):
	if request.method == 'POST':
		user_form = LoinForm()
		user_auth = authenticate(request, username=request.POST['username'], password = request.POST['password'])
		if user_auth is not None:
			login(request, user_auth)
			return redirect('user_app:profile')
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
	logout(request)
	data = {
		'page_name': 'logout',
	}
	return render(request, 'user_app/logout.html', data)


def register_user(request):
	if request.method == 'POST':
		user_form = UserCreationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit= False)
			new_user.set_password(user_form.cleaned_data['password1'])
			new_user.save()
			messages.success(request, f'congratulation {user_form.cleaned_data["username"]} registration had been successfully')
			return redirect('user_app:login')
	else:
		user_form = UserCreationForm()
	data = {
		'page_name': 'register'.title(),
		'user_form': user_form,
	}
	return render(request, 'user_app/register.html', data)


@login_required(login_url='user_app:login')
def profile_user(request):
	data = {
		'page_name': 'profile'.title(),
		'db_posts_objects': models.Post.objects.filter(author=request.user)
	}
	return render(request, 'user_app/profile.html', data)


def update_profile(request):
	data = {
		'page_name': 'update profile'.title(),
	}
	return render(request, 'user_app/update_profile.html', data)

