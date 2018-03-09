from django.urls import path
from . import views


urlpatterns = [
    path('', views.questions, name='questions'),
    #path('hot/'),
    #path('question/'),
    #path('ask/')
]
