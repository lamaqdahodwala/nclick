from .serializers import GameSerializer
from ..models import Game
from rest_framework.response import Response
from rest_framework.views import APIView

class GetGameDataView(APIView):
    def get(self, req):
        ...