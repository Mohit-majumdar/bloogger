"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from Blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',Home, name='home'),
    url(r'^about',about, name='about'),
    url(r'^lifestyle/$',lifestyle,name='lifestyle'),
    url(r'^fashion/$',fashion,name='fashion'),
    url(r'^contact/$',contact,name='contact'),
    url(r'Login/$',Login,name='Login'),
    url(r'singup/$',Singup,name='singup'),
    url(r'logout/$',Logout,name='logout'),
    url(r'post_like/(?P<pid>[0-9]+)/$',blog_life,name='like'),
    url(r'^blogdetail/(?P<bid>[0-9]+)/$',blogdetail,name='blogdetail'),
    url(r'allcat/$',all_cat,name='allcat'),
    url(r'^AddPost/$',add_post,name='addpost'),
    url(r'comment/(?P<bid>[0-9]+)/$',blog_comment,name='blogcooment'),
    url(r'^userdetail/$',userdetails,name='userdetail'),
    url(r'^delete/(?P<bid>[0-9]+)/$',delete_blog,name='delete'),
    url(r'^catigorypot/(?P<cid>[0-9]+)/$',catygiory_post,name='catigorypost')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
