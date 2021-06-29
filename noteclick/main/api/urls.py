from django.urls import path

from noteclick.main.api import views

urlpatterns = [
    path('gamedata', views.GetGameData.as_view()),
    path('new_game', views.CreateNewGame.as_view())
]