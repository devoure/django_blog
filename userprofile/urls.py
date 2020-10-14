from django.urls import re_path
from userprofile import views

urlpatterns =[
    re_path(r'^profile/$', views.user_profile)]
