from django.urls import path
from . import views

app_name = 'league'
urlpatterns = [
    path('', views.index, name='index'),
]