from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('', views.login, name='login'),
    path('',views.index),
    path('login/',views.login),
    path('list/',views.list),
    path('base/',views.base),
    path('statistic/',views.statistic)
]