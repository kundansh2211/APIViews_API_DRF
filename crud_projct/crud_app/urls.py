from django.urls import path
from .views import MobileAPI

urlpatterns = [
    path('mobile/', MobileAPI.as_view()),
    path('mobile/<int:pk>', MobileAPI.as_view())
]