from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acervo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="livro",
            options={"ordering": ["titulo"], "verbose_name": "Livro", "verbose_name_plural": "Livros"},
        ),
        migrations.AddField(
            model_name="livro",
            name="tipo_acervo",
            field=models.CharField(
                choices=[("DIGITAL", "Digital"), ("FISICO", "Físico")],
                default="FISICO",
                max_length=10,
                verbose_name="Tipo de acervo",
            ),
        ),
        migrations.AddField(
            model_name="livro",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("000", "000 – Generalidades e Informação"),
                    ("100", "100 – Filosofia e Psicologia"),
                    ("200", "200 – Religião e Teologia"),
                    ("300", "300 – Ciências Sociais e Direito"),
                    ("400", "400 – Linguística e Idiomas"),
                    ("500", "500 – Ciências Puras (Exatas e Naturais)"),
                    ("600", "600 – Ciências Aplicadas (Tecnologia)"),
                    ("700", "700 – Artes e Recreação"),
                    ("800", "800 – Literatura"),
                    ("900", "900 – História e Geografia"),
                ],
                default="000",
                max_length=3,
                verbose_name="Categoria",
            ),
        ),
    ]
