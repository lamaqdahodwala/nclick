from django.http.response import HttpResponseRedirect
from .serializers import GameSerializer
from ..models import Game
from rest_framework.response import Response

from rest_framework.views import APIView


class GetGameDataView(APIView):
    def get(self, req):
        if req.user.is_authenticated:
            try:
                game: Game = Game.objects.get(user=req.user)
            except:
                game = Game.objects.create(user=req.user)

            ser = GameSerializer(game)
            return Response(ser.data)
        else:
            return HttpResponseRedirect('/')