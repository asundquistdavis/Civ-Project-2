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