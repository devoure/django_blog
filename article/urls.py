from django.urls import re_path
from article import views
from django_test import settings
from django.conf.urls.static import static
urlpatterns =[
              re_path(r'^all/$', views.articles,name = 'index'),
              re_path(r'^get/(?P<article_id>\d+)/$', views.article, name = 'index1'),
              re_path(r'^language/(?P<language>[a-z\ -]+)/$', views.language),
              re_path(r'^create/$', views.create),
              re_path(r'^like/(?P<article_id>\d+)/$', views.like_article),
              re_path(r'^add_comment/(?P<article_id>\d+)/$', views.add_comment),
              re_path(r'^search/$', views.search_titles)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

