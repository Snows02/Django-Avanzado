"""Circles urls."""

# Django
from django.urls import path

# Views
from cride.users.views.users import UserLoginAPIView

urlpatterns = [
    path('user/login/', UserLoginAPIView.as_view(), name='login'),
]