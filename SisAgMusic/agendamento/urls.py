from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_professor/', views.cadastrar_professor, name='cadastrar_professor'),
    path('lista_professores/', views.lista_professores, name='lista_professores')
]
