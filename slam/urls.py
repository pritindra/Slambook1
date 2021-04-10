from django.urls import path
from slam import views

urlpatterns = [
    path('/',views.home, name='home'),
]