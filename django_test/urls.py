"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path, re_path
from article import views
from article.views import HelloTemplate
from django.urls import include, path
from django_test import views as auth_views
from django_test.forms import ContactForm1, ContactForm2, ContactForm3
from django_test.views  import ContactWizard
import settings

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^hello/$', views.hello),
    re_path(r'^hello_template/$' , views.hello_template),
    re_path(r'^hello_class_view/$', HelloTemplate.as_view()),
    re_path(r'^articles/', include('article.urls')),
    re_path(r'^accounts/', include('userprofile.urls')),
    re_path(r'^accounts/login/$', auth_views.login),
    re_path(r'^accounts/auth$', auth_views.auth_view),
    re_path(r'^accounts/logout/$', auth_views.logout),
    re_path(r'^accounts/loggedin/$', auth_views.loggedin),
    re_path(r'^accounts/invalid/$', auth_views.invalid_login),
    re_path(r'^accounts/register/$', auth_views.register_user),
    re_path(r'^accounts/register_success/$', auth_views.register_success),
    re_path(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3]))






]

if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
