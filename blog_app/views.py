from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.


def detail(request, question_id):
	question = get_object_or_404(models.Post, pk=question_id)
	return render(request, '', {'question': question})


def home(request):
	data = {
		'page_name': 'home'.title(),
		'db_objects_posts': models.Post.objects.all().order_by('-date_update')[:5],
		'db_objects_posts_3': models.Post.objects.all().order_by('-date_update')[:3],
	}
	return render(request, 'blog_app/home.html', data)


def about(request):
	return render(request, 'blog_app/about.html')


def details(request, post_id):
	data = {
		'page_name': 'post-details',
		'current_post': get_object_or_404(models.Post, pk=post_id),
	}
	return render(request, 'blog_app/details.html')


def delete_post(request):
	return render(request, 'blog_app/delete_post.html')


def new_post(request):
	return render(request, 'blog_app/new_post.html')


def update_post(request):
	return render(request, 'blog_app/update_post.html')


def user_posts(request):
	return render(request, 'blog_app/user_posts.html')
