from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_livros, name="lista"),
    path("livros/", views.lista_livros, name="livros"),
]
