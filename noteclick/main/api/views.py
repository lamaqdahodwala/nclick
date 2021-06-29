from django.shortcuts import get_object_or_404
from .serializers import GameSerializer
from ..models import Game
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_game_data(req):
    game = get_object_or_404(Game, user=req.user)
    ser = GameSerializer(game)
    return Response(ser.data)
