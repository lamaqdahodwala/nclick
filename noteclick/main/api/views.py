from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import GameSerializer
from ..models import Game
from rest_framework.response import Response
from rest_framework.decorators import api_view


class GetGameData(APIView):
    http_method_names = ["GET"]

    def get(self, req):
        if req.user.is_authenticated:
            game = get_object_or_404(Game, user=req.user)
            ser = GameSerializer(game)
            return Response(ser.data)


class CreateNewGame(APIView):
    http_method_names = ["POST"]
    def post(self, req):
        if req.user.is_authenticated:
            game = Game()
            game.user = req.user
            game.save()