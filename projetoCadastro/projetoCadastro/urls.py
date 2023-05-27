from django.urls import path

from appCadastro import views

urlpatterns = [
    # caminho, view, nome de referência
    path('', view.home, name='home')
]
