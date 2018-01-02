from django.urls import path

from . import views

urlpatterns = [
    path('pdf-generator/', views.pdf_generator, name='pdf-generator'),
]