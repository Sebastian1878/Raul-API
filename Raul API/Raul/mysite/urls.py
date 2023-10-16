from django.urls import path
from .views import fibo_view

urlpatterns = [
    path('fibonacci/<int:n>/', fibo_view),
]
