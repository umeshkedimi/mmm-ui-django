from django.contrib import admin
from django.urls import path
from main.views import home_view, about_view, features_view, contact_view


urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('features/', features_view, name='features'),
    path('contact/', contact_view, name='contact'),
]
