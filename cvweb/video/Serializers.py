from rest_framework import serializers
from .models import XpcVideo

class VideoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = XpcVideo
        fields = ('id','title','video','jianjie','video_type','create_time','cover')
