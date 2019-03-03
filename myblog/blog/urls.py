# _*_ encoding:utf-8 _*_
__author__ = 'listen'
__date__ = '2019/2/28 21:48'
from django.conf.urls import url
from blog import views
app_name='blog'
urlpatterns = [
    url(r'^index/$',views.index,name="home"),
    url(r'^add/$', views.add_page, name="add_page"),
    url(r'^article/(?P<article_id>[0-9]+)/$',views.article_page,name="article_page"),
    url(r'^edit/(?P<article_id>[0-9]+)/$',views.edit_page,name="edit_page"),
    url(r'^edit/action/(?P<article_id>[0-9]+)/$',views.edit_action,name="edit_action"),

]
