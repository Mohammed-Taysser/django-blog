from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . forms import NewComment
# Create your views here.


def home(request):
	data = {
		'page_name': 'home'.title(),
		'db_objects_posts': models.Post.objects.all().order_by('-date_update')[:5],
		'db_objects_posts_3': models.Post.objects.all().order_by('-date_update')[:3],
		'db_objects_comments': models.Comment.objects.filter(active=True),
	}
	return render(request, 'blog_app/home.html', data)


def about(request):
	return render(request, 'blog_app/about.html')


def details(request, post_id):
	current_post = get_object_or_404(models.Post, pk=post_id)
	comment_form = NewComment()
	if request.method == 'POST':
		comment_form = NewComment(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = current_post
			new_comment.save()
			comment_form = NewComment()
	data = {
		'current_post': current_post,
		'page_name': current_post.title.title(),
		'db_objects_posts': models.Post.objects.all()[:5],
		'db_objects_comments': current_post.comment.filter(active=True),
		'comment_form': comment_form,
	}
	return render(request, 'blog_app/post_details.html', data)


def delete_post(request):
	return render(request, 'blog_app/delete_post.html')


def new_post(request):
	return render(request, 'blog_app/new_post.html')


def update_post(request):
	return render(request, 'blog_app/update_post.html')


def user_posts(request):
	return render(request, 'blog_app/user_posts.html')
