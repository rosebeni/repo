
from django.urls import path
from . import views

urlpatterns = [
        path('myprojects/my_tennis_club/members/', views.members, name='members'),
]
