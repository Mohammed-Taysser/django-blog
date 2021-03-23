from django.shortcuts import render
from .forms import UserCreationForm

# Create your views here.
app_name = 'user_app'


def login(request):
	return render(request, 'user_app/login.html')


def logout(request):
	return render(request, 'user_app/logout.html')


def profile(request):
	return render(request, 'user_app/profile.html')


def update_profile(request):
	return render(request, 'user_app/update_profile.html')


def register(request):
	data = {
		'page_name': 'register'.title(),
		'user_form': UserCreationForm(),
	}
	return render(request, 'user_app/register.html', data)
