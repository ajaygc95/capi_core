from django.urls import path
from .views import FacebookWebhook

urlpatterns = [
     path("", FacebookWebhook.as_view(), name="fb-webhook"),
]
