"""cvweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from video import views as video_views
from comic import views as comic_views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from . import settings



router = routers.DefaultRouter()
router.register(r'video', video_views.VideoViewSet) #视频接口
router.register(r'comic',comic_views.ComicViewSet)
#router.register(r'chapter',comic_views.ChapterViewSet)
#router.register(r'page',comic_views.PageViewSet)


urlpatterns = [
    #path('',TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/chapter',comic_views.ChapterList.as_view()), #具体漫画接口
    path('api/page',comic_views.PageViewSet.as_view()),
    #path('video/',TemplateView.as_view(template_name="video.html")),
    #path('comic/',TemplateView.as_view(template_name="comic.html")),
  

]
urlpatterns += static('/media/', document_root=settings.STATIC_ROOT)

