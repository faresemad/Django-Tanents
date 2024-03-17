from django.urls import path

from app.api.views import create_domain

urlpatterns = [
    path('create-domain/', create_domain, name='create-domain'),
]
