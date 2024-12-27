from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_files, name='upload_files'),
    path('descargar/<str:carpeta>/', views.descargar_documentos, name='descargar_documentos'),
    path('descargar_plantilla/', views.descargar_plantilla, name='descargar_plantilla'),
]
