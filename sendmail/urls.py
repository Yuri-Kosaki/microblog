from django.urls import path
from . import views

appname = 'sendmail'
urlpatterns = [
    path('', views.index, name='index'),
]
