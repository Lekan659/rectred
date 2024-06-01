from django.urls import path
from .views import verify_captcha

urlpatterns = [
    path('verify-captcha/', verify_captcha),
]