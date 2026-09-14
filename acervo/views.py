from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import LivroForm
from .models import Livro


def lista_livros(request):
    busca = request.GET.get("q", "").strip()
    tipo = request.GET.get("tipo", "").strip()
    categoria = request.GET.get("categoria", "").strip()

    livros = Livro.objects.all()

    if busca:
        livros = livros.filter(
            Q(titulo__icontains=busca) | Q(autor__icontains=busca)
        )

    if tipo:
        livros = livros.filter(tipo_acervo=tipo)

    if categoria:
        livros = livros.filter(categoria=categoria)

    context = {
        "livros": livros,
        "busca": busca,
        "tipo_selecionado": tipo,
        "categoria_selecionada": categoria,
        "tipos": Livro.TipoAcervo.choices,
        "categorias": Livro.CATEGORIAS,
    }
    return render(request, "acervo/lista.html", context)


def novo_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista")
    else:
        form = LivroForm()

    return render(request, "acervo/form.html", {"form": form})
