import json
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
import requests
from django.conf import settings

from .serializers import ArticleSerializer
from .models import BaseModel
from .services import WbCardService


class WbCardViewSet(
    GenericViewSet
):
    serializer_class = ArticleSerializer
    queryset = BaseModel.objects.all()
    service = WbCardService()

    @action(methods=['POST'], detail=False)
    def article_file(self, request):
        data = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data['articles'] = self.service.data_prep(serializer.validated_data)
        response = requests.post(
            f"http://{settings.AIOHTTP_HOST}:{settings.AIOHTTP_PORT}/get_data_by_article",
            json=json.dumps(data)
        )
        return Response(response.json(), status=status.HTTP_200_OK)
