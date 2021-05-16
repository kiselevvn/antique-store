from django.urls import path
from .programming_interface import OrderCreateAPIView

urlpatterns = [
    path("create/", OrderCreateAPIView.as_view()),
]
