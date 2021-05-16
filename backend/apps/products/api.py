from django.urls import path
from .programming_interface import ProductRetriveAPIView

urlpatterns = [
    path("retrive/<int:pk>/", ProductRetriveAPIView.as_view()),
]
