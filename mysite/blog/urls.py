from django.urls import path
from .views.post_view import PostView  # Importa corretamente a view

urlpatterns = [
    path('', PostView.as_view(), name='home'),  # Apenas uma declaração de urlpatterns
]
