# CookiesLab Web

Web completa para **CookiesLab**, emprendimiento estudiantil de galletas en Saltillo, Coahuila. Construida con Django + MySQL + Tailwind CSS. Pedidos directamente por WhatsApp.

## Stack

| Capa | Tecnología |
|------|-----------|
| Backend | Python 3.11+ / Django 5.x |
| Base de datos | MySQL / MariaDB (XAMPP) |
| Frontend | Tailwind CSS CDN + JS vanilla |
| Admin | Django Admin nativo |
| Pedidos | WhatsApp (`wa.me`) |

## Características

- Landing con hero editable, productos destacados, promos y CTA
- Menú/catálogo con filtro de categorías (JS)
- Carrito de pedido con generador de link WhatsApp
- Panel de carrito mobile (drawer desde la barra inferior)
- Estados de producto: Disponible · Preventa · Agotado · Oculto
- Página de promociones y giveaways
- Formulario de pedido opcional que guarda en DB
- Admin completo con previsualizaciones de imagen
- Configuración del negocio 100% editable desde admin
- `seed_demo` con 9 productos y 3 promos listas

## URLs

| Ruta | Descripción |
|------|-------------|
| `/` | Landing / Home |
| `/menu/` | Catálogo de productos + carrito |
| `/promos/` | Promociones y giveaways |
| `/pedido/` | Formulario de pedido (guarda en DB) |
| `/admin/` | Panel de administración |

---

## Arranque en Windows (XAMPP / Navicat)

### 1. Ir a la carpeta del proyecto

```cmd
cd /d C:\x\CookiesLab-Web
```

### 2. Crear entorno virtual e instalar dependencias

```cmd
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> Si `mysqlclient` falla en Windows, instala primero las dependencias de compilación
> o usa `PyMySQL` (ya incluido en requirements.txt — el settings.py lo activa automáticamente):
> ```cmd
> pip install PyMySQL
> ```

### 3. Crear la base de datos

En Navicat, MySQL Workbench o la consola de XAMPP:

```sql
CREATE DATABASE cookieslab_web CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Configurar variables de entorno

```cmd
copy .env.example .env
```

Edita `.env` con tus datos (el valor de `DB_PASSWORD` puede quedar vacío si usas XAMPP sin contraseña):

```env
SECRET_KEY=cambia-esto-por-una-clave-segura
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=cookieslab_web
DB_USER=root
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=3306
```

> Si XAMPP usa el puerto **3307** en lugar del estándar:
> ```env
> DB_PORT=3307
> ```

### 5. Generar y aplicar migraciones

```cmd
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario para el admin

```cmd
python manage.py createsuperuser
```

### 7. Cargar datos demo

```cmd
python manage.py seed_demo
```

Crea: configuración del negocio · 4 categorías · 9 productos (disponibles, preventa y agotados) · 3 promociones.

> **Después de seed_demo**, entra a `/admin/` → *Configuración del negocio* y reemplaza el número de WhatsApp demo `528441234567` con el número real.

### 8. Correr el servidor

```cmd
python manage.py runserver
```

Abre en el navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Comandos de referencia rápida

```cmd
# Activar entorno (si cerraste la terminal)
.venv\Scripts\activate

# Instalar dependencias nuevas
pip install -r requirements.txt

# Migrar después de cambiar modelos
python manage.py makemigrations
python manage.py migrate

# Correr servidor de desarrollo
python manage.py runserver

# Limpiar y volver a sembrar demo (idempotente)
python manage.py seed_demo
```

---

## Admin — Qué puede hacer el administrador

| Sección | Acciones |
|---------|---------|
| Configuración del negocio | Editar nombre, slogan, WhatsApp, Instagram, ubicación, textos del hero, notas de entrega, logo |
| Categorías | Crear/editar/ordenar/ocultar |
| Productos | Crear/editar, subir foto, cambiar precio, cambiar estado, marcar como destacado |
| Pedidos | Ver pedidos, cambiar estado (Pendiente/Confirmado/Entregado/Cancelado), link directo a WhatsApp del cliente |
| Promociones | Crear promos con imagen, fecha de inicio/fin, activar/desactivar |

---

## Estructura del proyecto

```text
CookiesLab-Web/
├── config/           → settings, urls, wsgi, asgi
├── apps/
│   ├── core/         → Home (landing)
│   ├── catalog/      → Categorías, Productos, seed_demo
│   ├── orders/       → Pedidos, formulario
│   ├── promos/       → Promociones y giveaways
│   └── site_settings/→ Configuración editable del negocio
├── templates/        → Todos los templates HTML
├── static/
│   ├── css/app.css   → Estilos custom + Tailwind helpers
│   └── js/cart.js    → Carrito, filtro categorías, drawer mobile
├── media/            → Uploads (imágenes de productos, promos, logo)
├── .env.example      → Variables de entorno (copia a .env)
└── manage.py
```

---

## Checklist para producción

- [ ] `DEBUG=False` en `.env`
- [ ] `SECRET_KEY` cambiada a una clave segura aleatoria
- [ ] `ALLOWED_HOSTS` configurado con el dominio real
- [ ] Archivos estáticos servidos con WhiteNoise o nginx (`python manage.py collectstatic`)
- [ ] Media files configurados en el hosting
- [ ] Respaldos automáticos de MySQL
- [ ] Número de WhatsApp real en Admin → Configuración
- [ ] Logo del negocio subido en Admin → Configuración
