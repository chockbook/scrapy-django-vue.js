from django.shortcuts import render
from .Serializers import ChapterSerializers,PageSerializers,ComicSerializers
from rest_framework import viewsets,generics
from .models import Comic,Chapter,Page
from rest_framework import permissions
from rest_framework.response import Response



class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ChapterList(generics.ListAPIView):
    serializer_class = ChapterSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #get_queryset
    def get_queryset(self):
        queryset = Chapter.objects.all()
        comic = self.request.query_params.get('comic',None) #获取参数query_params
        if comic is not None:
            queryset = queryset.filter(comic=comic)
        return queryset


class PageViewSet(generics.ListAPIView):
    
    serializer_class = PageSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Page.objects.all()
        chapter = self.request.query_params.get('chapter',None)
        if chapter is not None:
            queryset = queryset.filter(chapter=chapter).order_by('id')
        return queryset













# Create your views here.
