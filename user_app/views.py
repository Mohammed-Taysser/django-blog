from django.shortcuts import render


# Create your views here.


def login(request):
	return render(request, 'user_app/login.html')


def logout(request):
	return render(request, 'user_app/logout.html')


def profile(request):
	return render(request, 'user_app/profile.html')


def update_profile(request):
	return render(request, 'user_app/update_profile.html')


def register(request):
	return render(request, 'user_app/register.html')
