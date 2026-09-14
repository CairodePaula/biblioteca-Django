from django import forms
from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "autor", "ano", "disponivel", "tipo_acervo", "categoria"]
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Nome do livro"}),
            "autor": forms.TextInput(attrs={"placeholder": "Autor"}),
            "ano": forms.NumberInput(attrs={"min": 0}),
        }
