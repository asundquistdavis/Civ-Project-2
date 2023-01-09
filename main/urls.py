from django.urls import path
from . import views
from game.models import Game

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile page'),
    path('newgame/', views.newgame, name='start new game'),
    path('playgame/<int:id>/', views.playgame, name='play game'),
]