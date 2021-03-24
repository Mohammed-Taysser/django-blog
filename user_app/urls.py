from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
	path('', views.profile_user, name='profile'),
	path('login', views.login_user, name='login'),
	path('logout', views.logout_user, name='logout'),
	path('register', views.register_user, name='register'),
	path('update-profile', views.update_profile, name='update_profile'),
]
