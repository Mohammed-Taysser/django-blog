from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog_app import models
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
	db_posts_objects = models.Post.objects.filter(author=request.user)
	paginator = Paginator(db_posts_objects, 20)
	current_page = request.GET.get('page')
	try:
		db_posts_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_posts_objects = paginator.page(1)
	except EmptyPage:
		db_posts_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'profile'.title(),
		'db_posts_objects': db_posts_objects,
		'db_posts_objects_number': models.Post.objects.filter(author=request.user),
		'page': current_page,
	}
	return render(request, 'user_app/profile.html', data)

@login_required(login_url='user_app:login')
def update_profile(request):
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST ,instance=request.user)
		user_profile_image = ProfileUpdateImage(request.POST, request.FILES, instance=request.user.userprofile)
		if user_form.is_valid() and user_profile_image.is_valid():
			user_form.save()
			user_profile_image.save()
			messages.success(request, 'profile update')
			return redirect('user_app:profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		user_profile_image = ProfileUpdateImage(instance=request.user.userprofile)
	data = {
		'page_name': 'update profile'.title(),
		'user_form': user_form,
		'user_profile_image': user_profile_image,
		'user_v': user_profile_image.is_valid()
	}
	return render(request, 'user_app/update_profile.html', data)

