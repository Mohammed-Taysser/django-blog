from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . forms import NewComment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class PostCreateView(LoginRequiredMixin, CreateView):
	model = models.Post
	fields = ['title', 'content']
	template_name = 'blog_app/new_post.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
	model = models.Post
	fields = ['title', 'content']
	template_name = 'blog_app/update_post.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		current_post = self.get_object()
		if self.request.user == current_post.author:
			return True
		else:
			return False

def home(request):
	db_objects_posts = models.Post.objects.all().order_by('-date_update')
	paginator = Paginator(db_objects_posts, 5)
	current_page = request.GET.get('page')
	try:
		db_objects_posts = paginator.page(current_page)
	except PageNotAnInteger:
		db_objects_posts = paginator.page(1)
	except EmptyPage:
		db_objects_posts = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'home'.title(),
		'db_objects_posts': db_objects_posts,
		'db_objects_comments': models.Comment.objects.filter(active=True),
		'page': current_page,
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
