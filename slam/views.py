from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from slam.models import Slam


def slampage(request):
    if request.method == 'POST':
        username = request.POST['username']
        nickname = request.POST['nickname']
        email = request.POST['email']
        petname = request.POST['petname']
        zodiac = request.POST['zodiac']
        birthday = request.POST['birthday']
        hobbies = request.POST['hobbies']

        ambition = request.POST['ambition']
        films = request.POST['films']
        actors = request.POST['actors']
        songs = request.POST['songs']
        books = request.POST['books']
        reality_show = request.POST['reality_show']
        singer = request.POST['singer']

        friends = request.POST['friends']
        crush = request.POST['crush']
        fantasy = request.POST['fantasy']
        notes = request.POST['notes']
        feature = request.POST['feature']
        lifeline = request.POST['lifeline']
        fear = request.POST['fear']
        power = request.POST['power']
        lines_for = request.POST['lines_for']

        slam = Slam.objects.create(username=username, nickname=nickname, email=email, birthday=birthday,zodiac=zodiac,hobbies=hobbies,
                ambition=ambition, films=films, actors=actors, songs=songs, books=books, reality_show=reality_show,singer=singer,
                friends=friends, crush= crush, fantasy=fantasy, notes=notes, feature=feature, lifeline=lifeline,fear=fear,
                power=power, lines_for= lines_for)
        slam.save()
        return redirect('signin')

    else:
        return render(request, 'slam/slampage.html')

class SlamListView(ListView,LoginRequiredMixin):
    model = Slam
    template_name = 'slam/slamlist.html'
    context_object_name = 'slams'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class SlamMoreInfo(DetailView,LoginRequiredMixin):
    model = Slam
    template_name = 'interface/more_info.html'
    context_object_name = 'slams'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data