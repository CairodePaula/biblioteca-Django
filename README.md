# Biblioteca — Consolidado das Aulas 04 e 05

Projeto Django de gerenciamento de acervo de livros, desenvolvido na disciplina
**Laboratório de Programação Full Stack** (Universidade de Vassouras).

- **Aula 04:** projeto, app, model, PostgreSQL, migrações, ORM e Django Admin.
- **Aula 05:** views, URLs, templates, herança de templates e ModelForm.

## Funcionalidades

- Cadastro de livros (título, autor, ano, disponibilidade).
- **Tipo de acervo:** Digital ou Físico.
- **Categoria (CDD):** 000 a 900.
- **Pesquisa por nome** (título ou autor), **por tipo de acervo** e **por categoria** — filtros combináveis.
- Listagem em cards, com mensagem para lista vazia.
- Django Admin com busca (`search_fields`) e filtros (`list_filter`).

### Categorias utilizadas

| Código | Área |
|--------|------|
| 000 | Generalidades e Informação |
| 100 | Filosofia e Psicologia |
| 200 | Religião e Teologia |
| 300 | Ciências Sociais e Direito |
| 400 | Linguística e Idiomas |
| 500 | Ciências Puras (Exatas e Naturais) |
| 600 | Ciências Aplicadas (Tecnologia) |
| 700 | Artes e Recreação |
| 800 | Literatura |
| 900 | História e Geografia |

## Tecnologias

Python 3.10+ · Django 5 · PostgreSQL · python-dotenv · HTML/CSS

## Como executar

### 1. Ambiente virtual e dependências

Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Banco de dados

```sql
CREATE DATABASE biblioteca_db;
```

Copie `.env.example` para `.env` e ajuste os valores:

```env
DB_NAME=biblioteca_db
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=troque-esta-chave
```

O arquivo `.env` está no `.gitignore` e nunca deve ser versionado.

### 3. Migrações e execução

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Rotas

| Rota | Descrição |
|------|-----------|
| `/` e `/livros/` | Listagem do acervo com pesquisa e filtros |
| `/livros/novo/` | Cadastro de livro |
| `/admin/` | Django Admin |

Exemplo de pesquisa combinada: `/?q=machado&tipo=FISICO&categoria=800`

## Estrutura

```
biblioteca/
├── manage.py
├── requirements.txt
├── .env.example
├── biblioteca/          # configurações do projeto
│   ├── settings.py
│   └── urls.py
└── acervo/              # app do acervo
    ├── models.py        # model Livro (tipo de acervo + categoria)
    ├── views.py         # listagem com pesquisa e cadastro
    ├── forms.py         # LivroForm (ModelForm)
    ├── urls.py          # rotas do app (criado manualmente)
    ├── admin.py
    ├── migrations/
    ├── templates/acervo/
    └── static/acervo/
```
