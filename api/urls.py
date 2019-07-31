from datetime import datetime
import uuid

from django.conf.urls import url, include
from django.db import models
from django.urls import path
from django.utils import timezone
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UrlList, UrlDetail


urlpatterns = [
    path("urls", UrlList.as_view()),
    path("urls/<str:pk>/", UrlDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
