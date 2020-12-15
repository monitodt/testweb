from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name= 'home'),
    path('polis',views.polis, name='polis'),
    path('help',views.help, name='help'),
    path('create',views.create, name='create')
]