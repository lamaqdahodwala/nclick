from django.urls import path
from . import views

urlpatterns = [
    path("get_game", views.GetGameDataView.as_view()),
    path('save', views.SaveGameView.as_view())
]
