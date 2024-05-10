from django.urls import path
from . import views


urlpatterns = [
    path('', views.menuPage, name='menu'),
    path('<int:id>/', views.menuDetail, name='menu_detail')
]