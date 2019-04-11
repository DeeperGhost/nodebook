from django.urls import path
from . import views
from .views import *
urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('', views.login, name='login'),
    # path('',views.index),
    path('', listView.as_view(), name='my-view'),
    path('login/',views.login),
    path('list/',views.list),
    path('base/',views.base),
    path('statistic/',views.statistic)
]