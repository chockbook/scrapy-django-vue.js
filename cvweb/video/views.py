from django.shortcuts import render
from .Serializers import VideoSerializers
from rest_framework import viewsets
from .models import XpcVideo
from rest_framework import permissions


class VideoViewSet(viewsets.ModelViewSet):
    queryset = XpcVideo.objects.all()
    serializer_class = VideoSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)











# Create your views here.
