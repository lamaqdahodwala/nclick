from django.http.response import HttpResponseBadRequest
from .serializers import GameSerializer
from ..models import Game
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
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
            return HttpResponseBadRequest()

class SaveGameView(APIView):
    def post(self, req):
        if req.user.is_authenticated:
            data = req.data
            ser = GameSerializer(data=data)
            pts = ser.data.get('pts')
            cps = ser.data.get('cps')
            model : Game = Game.objects.get(user=req.user)
            model.points = pts
            model.cps = cps
            model.save()
            
        