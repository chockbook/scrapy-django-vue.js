from django.db import models

# Create your models here.


class XpcVideo(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    video = models.CharField(max_length=100, blank=True, null=True)
    jianjie = models.CharField(max_length=100, blank=True, null=True)
    video_type = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    cover = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xpc_video'
