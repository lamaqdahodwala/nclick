from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import GameSerializer
from ..models import Game
from rest_framework.response import Response
from rest_framework.decorators import api_view


class GetGameData(APIView):
    http_method_names = ["GET"]

    def get(self, req):
        game = get_object_or_404(Game, user=req.user)
        ser = GameSerializer(game)
        return Response(ser.data)
