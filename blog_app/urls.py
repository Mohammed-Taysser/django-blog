from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	path('details', views.details, name='details'),
	path('delete-post', views.delete_post, name='delete_post'),
	path('update-post', views.update_post, name='update_post'),
	path('user-posts', views.user_posts, name='user_posts'),
]
