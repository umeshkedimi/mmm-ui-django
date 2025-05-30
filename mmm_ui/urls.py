from django.contrib import admin
from django.urls import path
from main.views import home_view, about_view, features_view, contact_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('features/', features_view, name='features'),
    path('contact/', contact_view, name='contact'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])