from django.urls import path
from users import views
from users.views import (
    
    profile
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    # path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/<int:user_id>', profile.as_view(), name='profile')
]