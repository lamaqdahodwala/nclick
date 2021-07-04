from .serializers import GameSerializer
from ..models import Game
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class GetGameDataView(APIView):
    def get(self, req):
        if req.user.is_authenticated:
            game = get_object_or_404(Game, user=req.user)
