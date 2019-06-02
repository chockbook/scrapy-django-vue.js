from django.db import models

# Create your models here.

class Comic(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    intro = models.CharField(max_length=500, blank=True, null=True)
    cover = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comic'




class Chapter(models.Model):
    chapter = models.CharField(max_length=50, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    #comic = models.ForeignKey(Comic, models.DO_NOTHING, db_column='comic', blank=True, null=True)
    comic = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chapter'


class Page(models.Model):
    page_path = models.CharField(max_length=100, blank=True, null=True)
    page = models.CharField(max_length=100, blank=True, null=True)
    #chapter = models.ForeignKey(Chapter, models.DO_NOTHING, db_column='chapter', blank=True, null=True)
    chapter = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'page'




