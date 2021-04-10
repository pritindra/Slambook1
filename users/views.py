from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import sys
from users.models import UserInfo
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password==re_password:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            
            # Email verification
            # subject = 'Email verification from Insta-Blog'
            # message = 'Hey there! we have got your user request. A user has been created on this email.'
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [save_it.email, settings.EMAIL_HOST_USER]
            
            # send_mail(subject, message, from_email, to_list, fail_silently=True)

        else:
            messages.error(request, f'Password does not match')
            return redirect('register')

        return redirect('signin')

    else:
        return render(request, 'users/register.html')

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile', user_id=user.id)

        else:
            return redirect('signin')

    else:
        return render(request,'users/signin.html')

class profile(ListView,LoginRequiredMixin):
    model = UserInfo
    template_name = 'users/profile.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

def signout(request):
    auth.logout(request)
    return redirect('/')

# class UserList(ListView):
#     model = UserInfo
#     template_name = 'users/user-list.html'
#     context_object_name = 'users'
    