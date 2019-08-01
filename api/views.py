from random import randint

from django.http import Http404, HttpResponseBadRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Url
from .serializers import UrlSerializer

from word_service import get_next_giggle


class UrlList(APIView):
    # Uncomment for debugging purposes only
    # def get(self, request):
    #     urls = Url.objects.all()
    #     serializer = UrlSerializer(urls, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        if "url" not in request.data:
            return HttpResponseBadRequest("Missing url in request body")

        try:
            url = Url.objects.get(url=request.data["url"])
            serializer = UrlSerializer(url)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Url.DoesNotExist:
            data = {"url": request.data["url"]}

            serializer = UrlSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UrlDetail(APIView):
    def get_object(self, pk):
        try:
            return Url.objects.get(pk=pk)
        except Url.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        url = self.get_object(pk)
        serializer = UrlSerializer(url)
        return Response(serializer.data)
