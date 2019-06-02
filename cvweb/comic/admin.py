from django.contrib import admin
from .models import Comic,Chapter,Page

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','state')

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id','chapter',)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id',)

# Register your models here.
