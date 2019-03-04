from django.urls import path
from . import views



# path to help the user #
urlpatterns = [
    path('',views.index,name='index'),
    path('newuser/',views.newuser,name = 'newuser'),


]