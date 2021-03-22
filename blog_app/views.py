from django.shortcuts import render


# Create your views here.


def home(request):
	return render(request, 'blog_app/home.html')


def about(request):
	return render(request, 'blog_app/about.html')


def details(request):
	return render(request, 'blog_app/details.html')


def delete_post(request):
	return render(request, 'blog_app/delete_post.html')


def new_post(request):
	return render(request, 'blog_app/new_post.html')


def update_post(request):
	return render(request, 'blog_app/update_post.html')


def user_posts(request):
	return render(request, 'blog_app/user_posts.html')
