from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('editar/<int:id>/', EditarLivroView.as_view(), name='editar'),
]
