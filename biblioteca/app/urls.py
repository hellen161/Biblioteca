from django.urls import path
from .views import EditarLivroView  # ou ajuste o caminho

urlpatterns = [
    # outras rotas
    path('editar/<int:id>/', EditarLivroView.as_view(), name='editar'),
]
