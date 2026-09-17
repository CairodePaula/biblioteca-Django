# Biblioteca — Consolidado das Aulas 04 e 05

Projeto Django de gerenciamento de acervo de livros, desenvolvido na disciplina
**Laboratório de Programação Full Stack** — Universidade de Vassouras.

**Aluno:** Cairo de Paula Cunha Gomes  
**Professor:** Márcio Garrido  
**Disciplina:** Laboratório de Programação Full Stack — Eng.Soft06_B_N_M_991533_20262  
**Curso:** Engenharia de Software  

---

## Sobre o Projeto

Sistema web para gerenciamento de um acervo de livros, construído do zero com Django e PostgreSQL.

- **Aula 04:** ambiente virtual, projeto, app, model, migrações, ORM e Django Admin
- **Aula 05:** views, URLs, templates, herança de templates e ModelForm

---

## Funcionalidades

- Cadastro de livros (título, autor, ano, disponibilidade)
- **Tipo de acervo:** Digital ou Físico
- **Categoria (CDD):**

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

- **Pesquisa combinada** por nome/autor, tipo de acervo e categoria
- Listagem em cards com status de disponibilidade
- Django Admin com busca e filtros

---

## Tecnologias

- Python 3.10+
- Django 5
- PostgreSQL
- python-dotenv
- HTML / CSS

---

## Como executar

### 1. Ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Banco de dados

Crie o banco no PostgreSQL:
```sql
CREATE DATABASE biblioteca_db;
```

Copie o arquivo de exemplo e preencha com seus dados:
```bash
cp .env.example .env
```

```env
DB_NAME=biblioteca_db
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=troque-esta-chave
```

### 3. Migrações e execução

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Rotas

| Rota | Descrição |
|------|-----------|
| `/` | Listagem do acervo com pesquisa e filtros |
| `/livros/novo/` | Cadastro de livro |
| `/admin/` | Django Admin |

---

## Estrutura do Projeto

```
biblioteca/
├── manage.py
├── requirements.txt
├── .env.example
├── biblioteca/
│   ├── settings.py
│   └── urls.py
└── acervo/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── admin.py
    ├── migrations/
    ├── templates/acervo/
    └── static/acervo/
```
