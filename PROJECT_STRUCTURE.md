# Estructura del proyecto

```text
CookiesLab-Web-Starter/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── RUNBOOK.md
├── CLAUDE_PROMPT.md
├── PROJECT_STRUCTURE.md
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── catalog/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── management/commands/seed_demo.py
│   ├── orders/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── promos/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   └── models.py
│   └── site_settings/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── context_processors.py
│       └── models.py
├── templates/
│   ├── base.html
│   ├── core/home.html
│   ├── catalog/menu.html
│   ├── orders/create.html
│   └── orders/success.html
├── static/
│   ├── css/app.css
│   ├── js/cart.js
│   └── img/.gitkeep
├── media/
│   ├── product_images/.gitkeep
│   ├── promo_images/.gitkeep
│   └── brand/.gitkeep
└── docs/
    ├── feature_scope.md
    └── brand_reference.png
```

## Apps

### `core`
Páginas públicas generales: home, nosotros, contacto o landing.

### `catalog`
Categorías y productos.

### `orders`
Pedidos, clientes y detalle de productos solicitados.

### `promos`
Promociones, giveaways, colaboraciones y eventos.

### `site_settings`
Configuración editable desde admin: nombre, WhatsApp, Instagram, ubicación, textos principales y branding.
