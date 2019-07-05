from django.contrib import admin
from django.urls import path

from .views import emailView, successView

urlpatterns = [
	path('', emailView, name='send'),
	path('success/', successView, name='success'),
]