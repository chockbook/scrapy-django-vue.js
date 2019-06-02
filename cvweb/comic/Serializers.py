from rest_framework import serializers
from .models import Chapter,Comic,Page



class PageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('page_path','page','chapter')

class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id','chapter','data','comic')

class ComicSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comic
        fields = ('id','title','author','state','intro','cover')

