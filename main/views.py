from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from game.models import Game
from .models import User
from .forms import NewUser
from _thread import start_new_thread

def index(response):
    return HttpResponse('Test response')

def profile(response):
    return render(response, 'user/profile.html', {})

def users(response):
    return HttpResponse(User.objects.all())

def show_user(response, username):
    user = User.objects.filter(username=username)[:1].get()
    username = user.username
    password = user.password
    return HttpResponse(f'Username: {username}, Password: {password}')
    # return HttpResponse(username)

def new_user(response):
    if response.method == 'POST':
        form = NewUser(response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User(username=username, password=password)
            user.save()
        return HttpResponseRedirect(f'/user/{username}')
    else:
        form = NewUser()
    return render(response, 'main/newuser.html', {'form':form})

def newgame(response):
        game = Game()
        game.save()
        start_new_thread(game.run, ())
        return HttpResponseRedirect(f'/playgame/{game.id}')

def playgame(response, id):
    response.session['id']=id
    response.session.save()
    game = Game.objects.filter(id=id)[:1].get()
    user = response.user
    return render(response, 'game/play.html', {'game':game, 'player':user})