from shop.views import ViewTemplate
from django.urls import path

urlpatterns = [
    path("", ViewTemplate.as_view(), name='home')
]
