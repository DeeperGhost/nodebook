from django.urls import path
from . import views
from .views import *
urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('', views.login, name='login'),
    # path('',views.index),
    path('list/', listView.as_view(), name='my-view'),
    path('login/',views.login),
    # path('list/',views.list),
    path('', indexView.as_view(), name='indexView'),
    path('base/',views.base),

    path('post_edit/', views.post_new, name='post_new'),

    path('statistic/',views.statistic)
]