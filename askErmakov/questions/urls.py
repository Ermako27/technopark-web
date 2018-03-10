from django.urls import path
from . import views


urlpatterns = [
    path('', views.questions, name='questions'),
    path('ask/', views.ask, name='ask'),
    path('question/<title>/<text>', views.one_question_page, name='one_question_page'),
    path('tag/<tag>/', views.tag, name='tag'),
    path('hot/', views.very_hot, name='hot')
    #path('hot/'),
    #path('question/'),

]
