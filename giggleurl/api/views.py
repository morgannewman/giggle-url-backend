from random import randint

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Url
from .serializers import UrlSerializer


class UrlList(APIView):
    # def get(self, request):
    #     urls = Url.objects.all()
    #     serializer = UrlSerializer(urls, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        data = request.data
        data["url"] = str(randint(0, 1000000000))
        serializer = UrlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

