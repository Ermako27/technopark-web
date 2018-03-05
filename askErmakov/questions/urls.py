from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('hot/'),
    #path('question/'),
    #path('ask/')
]
