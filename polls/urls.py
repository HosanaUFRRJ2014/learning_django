from django.urls import path
from . import views

urlpatterns = [
                path('', views.index, name='index'),
                #path('', beginning_page.html, name='html'),
              ]
