# Prompt para Claude - Armar toda la web CookiesLab

Actúa como un desarrollador senior full-stack experto en **Django, MySQL, Tailwind CSS y diseño web comercial para negocios pequeños**.

Voy a darte un proyecto starter llamado **CookiesLab-Web-Starter**. Tu tarea es convertirlo en una web completa, funcional y vendible para el negocio **CookiesLab**, una marca estudiantil de galletas ubicada en **Saltillo, Coahuila**.

## Contexto del negocio

CookiesLab es un emprendimiento de galletas con estética juvenil/estudiantil. Su Instagram dice:

- Nombre: 『 ᴄᴏᴏᴋɪᴇꜱ ʟᴀʙ 』
- Ubicación: Saltillo, Coahuila
- Concepto: deliciosas galletitas que alegran el día
- Enfoque: de estudiantes para estudiantes
- También hacen dinámicas, promociones, mercaditos, giveaways y colaboraciones.

El proyecto debe quedar listo para venderse como una web real, no como demo escolar.

## Stack obligatorio

Usa:

- Python
- Django
- MySQL/MariaDB
- Navicat como gestor de base de datos
- Tailwind CSS por CDN o configuración simple
- Panel admin nativo de Django
- WhatsApp como canal principal de pedidos

No uses:

- React
- Vue
- Next.js
- django-allauth
- pagos reales en fase 1
- login de clientes todavía
- arquitecturas innecesariamente complejas

## Objetivo general

Construir una web donde el cliente pueda:

1. Ver una landing atractiva de CookiesLab.
2. Ver catálogo de galletas/productos.
3. Filtrar o distinguir productos disponibles, agotados y en preventa.
4. Seleccionar productos y cantidades.
5. Generar automáticamente un mensaje de WhatsApp con su pedido.
6. Enviar un formulario de pedido opcional que también se guarde en base de datos.
7. Ver promociones, giveaways o eventos activos.
8. Contactar por Instagram/WhatsApp.

Y donde el administrador pueda:

1. Crear/editar/eliminar productos.
2. Subir fotos.
3. Cambiar precios.
4. Marcar productos como disponible, agotado, preventa u oculto.
5. Administrar categorías.
6. Administrar promociones/giveaways.
7. Revisar pedidos.
8. Cambiar datos del negocio desde admin: WhatsApp, Instagram, ubicación, texto principal, horarios y notas de entrega.

## Prioridades del diseño

Quiero una web visualmente vendible:

- Estilo dulce, moderno y juvenil.
- Colores tipo cookie/chocolate/crema, con acentos vivos.
- Diseño responsive mobile-first.
- Hero fuerte con llamada a la acción.
- Cards de productos con foto, precio y estado.
- Botones claros: “Ver menú”, “Pedir por WhatsApp”, “Armar pedido”.
- Sección de promos/giveaways.
- Sección “De estudiantes para estudiantes”.
- Footer con Instagram, WhatsApp y ubicación.

No debe verse como plantilla genérica de Bootstrap.

## Funcionalidades mínimas obligatorias

### 1. Home

Ruta:

```text
/
```

Debe tener:

- Hero con nombre CookiesLab.
- Slogan editable desde admin.
- Botón “Ver menú”.
- Botón “Pedir por WhatsApp”.
- Productos destacados.
- Promos activas.
- Bloque “de estudiantes para estudiantes”.
- Bloque de ubicación/entregas.

### 2. Menú/catálogo

Ruta:

```text
/menu/
```

Debe mostrar:

- Categorías.
- Todos los productos activos.
- Foto, nombre, descripción, precio y estado.
- Input de cantidad o botones + / -.
- Botón para agregar al pedido.
- Resumen del pedido.
- Botón para enviar a WhatsApp.

### 3. Pedido por WhatsApp

Genera un mensaje como este:

```text
Hola, quiero hacer un pedido en CookiesLab 🍪

Productos:
- Galleta Red Velvet x2 - $70
- Brownie Cookie x1 - $45

Total estimado: $115

Nombre:
Lugar de entrega:
Hora:
Método de pago:
Notas:
```

El número de WhatsApp debe salir desde `BusinessSettings.whatsapp_number`.

El link debe usar:

```text
https://wa.me/52NUMERO?text=MENSAJE_URL_ENCODED
```

### 4. Formulario de pedido opcional

Ruta:

```text
/pedido/
```

Debe permitir guardar:

- Nombre
- Teléfono
- Lugar de entrega
- Fecha/hora deseada opcional
- Notas
- Productos y cantidades, si se implementa carrito en servidor
- Estado del pedido: pendiente, confirmado, entregado, cancelado

Si el flujo completo de carrito en base de datos tarda mucho, deja el formulario funcional y el carrito de WhatsApp en frontend.

### 5. Admin

Mejorar admin con:

- `list_display`
- `search_fields`
- `list_filter`
- `prepopulated_fields` para slugs
- acciones rápidas si aplica

Modelos esperados:

- `BusinessSettings`
- `Category`
- `Product`
- `Promotion`
- `CustomerOrder`
- `OrderItem`

### 6. Seed demo

Debe existir:

```cmd
python manage.py seed_demo
```

Y crear:

- Configuración del negocio.
- Categorías demo.
- Productos demo.
- Promociones demo.

### 7. Seguridad básica

- Usar `.env`.
- No subir `.env` a git.
- `DEBUG=True` solo en local.
- `SECRET_KEY` desde variable.
- Validaciones mínimas en formularios.
- No romper si falta configuración de negocio.

## Entregables esperados

Quiero que trabajes directamente sobre la estructura del starter y entregues:

1. Código completo funcionando.
2. Migraciones generadas.
3. Templates bonitos y responsive.
4. Admin funcional.
5. Seed demo funcional.
6. README actualizado con comandos reales.
7. Explicación breve de cambios realizados.
8. Lista de comandos exactos para correrlo en Windows con XAMPP/Navicat.

## Reglas de trabajo

- No destruyas la estructura existente; mejórala.
- Si un archivo ya existe, edítalo.
- Si falta un archivo, créalo.
- No inventes dependencias pesadas.
- Mantén el proyecto simple, claro y escalable.
- Prioriza que corra en localhost.
- Comenta solo lo necesario.
- No dejes código muerto.
- No dejes rutas rotas.
- No dejes templates sin conectar.

## Extra deseable

Si hay tiempo, agrega:

- Página `/promos/`.
- Badge visual para “agotado” y “preventa”.
- Botón flotante de WhatsApp.
- Contador/resumen de pedido sticky en mobile.
- Placeholders bonitos cuando no haya imagen.
- Sección para mercaditos/eventos.
- Soporte futuro para varios negocios: CookiesLab, raspados/yukis y rifas.

## Importante

Este proyecto se quiere vender a personas reales. Cuida el diseño, la experiencia y el lenguaje comercial. No lo dejes como tarea escolar.
