from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('pricing', views.pricing, name='pricing'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),
]
