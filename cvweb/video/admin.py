from django.contrib import admin
from .models import XpcVideo



@admin.register(XpcVideo)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id','title','video')
# Register your models here.
