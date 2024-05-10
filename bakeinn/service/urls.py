from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicePage, name='service'),
    path('<int:id>/', views.serviceDetail, name='service_detail')
]