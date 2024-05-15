from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogPage, name='blog'),
    path('<int:blog_id>/', views.blogDetail, name='blog_detail')
]
