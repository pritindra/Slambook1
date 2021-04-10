from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from slam.models import Slam

def home(request):
    pass

def slampage(request):
    if request.method == 'POST':
        name = request.POST['name']
        nickname = request.POST['nickname']

        slam = Slam.objects.create(username=username, nickname=nickname)
        slam.save()

    else:
        return render(request, 'slampage.html')

class SlamView(ListView,LoginRequiredMixin):
    model = Slam
    template_name = ''
    context_object_name = 'slams'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class SlamMoreInfo(DetailView,LoginRequiredMixin):
    model = Slam
    template_name = 'interface/more_info.html'
    context_object_name = 'slam'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data