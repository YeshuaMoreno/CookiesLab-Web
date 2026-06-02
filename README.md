# CookiesLab Web Starter 🍪

Starter en **Django + MySQL + Tailwind CDN** para construir una web vendible de CookiesLab: catálogo administrable, productos con estados, promociones, pedido por WhatsApp, formulario de pedidos y panel admin.

La idea es que Claude pueda tomar esta estructura y completar toda la web sin empezar desde cero.

## Stack

- Python 3.11+
- Django 5.x
- MySQL / MariaDB en XAMPP
- Navicat para administrar la base de datos
- Tailwind por CDN para avanzar rápido
- Admin nativo de Django
- WhatsApp como primer canal de pedido

## Estructura principal

```text
CookiesLab-Web-Starter/
├── manage.py
├── requirements.txt
├── .env.example
├── CLAUDE_PROMPT.md
├── PROJECT_STRUCTURE.md
├── RUNBOOK.md
├── config/
├── apps/
│   ├── core/
│   ├── catalog/
│   ├── orders/
│   ├── promos/
│   └── site_settings/
├── templates/
├── static/
├── media/
└── docs/
```

## Arranque rápido

```cmd
cd /d C:\x\CookiesLab-Web-Starter
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Crea una base de datos en Navicat/XAMPP:

```sql
CREATE DATABASE cookieslab_web CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Después:

```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```

URLs esperadas:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/menu/
http://127.0.0.1:8000/pedido/
http://127.0.0.1:8000/admin/
```

## Qué ya viene pensado

- Catálogo por categorías.
- Productos con foto, precio y estado: disponible, preventa, agotado, oculto.
- Promociones/giveaways administrables.
- Configuración del negocio desde admin: nombre, WhatsApp, Instagram, ubicación, texto hero, notas de entrega.
- Generador de mensaje para WhatsApp desde el menú.
- Formulario básico de pedido que guarda en base de datos.
- Seed demo con productos de ejemplo.

## Qué debe completar Claude

Lee `CLAUDE_PROMPT.md`. Ese archivo está hecho para pegarlo tal cual en Claude y pedirle que arme la web completa.
