from decimal import Decimal
from django.core.management.base import BaseCommand
from apps.catalog.models import Category, Product
from apps.promos.models import Promotion
from apps.site_settings.models import BusinessSettings


class Command(BaseCommand):
    help = 'Crea datos demo completos para CookiesLab.'

    def handle(self, *args, **options):
        self.stdout.write('Sembrando datos demo...')

        # ── Configuración del negocio ──────────────────────────
        business = BusinessSettings.get_solo()
        business.business_name = 'CookiesLab'
        business.slogan = 'deliciosas galletitas que alegrarán tu día \U0001f60b'
        business.hero_title = 'Galletitas recién hechas para alegrar tu día'
        business.hero_subtitle = (
            'De estudiantes para estudiantes. '
            'Arma tu pedido y mándalo directo por WhatsApp.'
        )
        business.location_text = 'Saltillo, Coahuila'
        business.delivery_notes = (
            'Entregas en puntos acordados, facultades y mercaditos según disponibilidad. '
            'Coordina horario y punto de entrega por WhatsApp.'
        )
        business.instagram_url = 'https://www.instagram.com/coookieslab/'
        business.whatsapp_number = '528443108356'
        business.save()
        self.stdout.write('  ✓ Configuración del negocio actualizada')

        # ── Categorías ────────────────────────────────────────
        cats = {
            'Clásicas':   Category.objects.get_or_create(name='Clásicas',  defaults={'order': 1})[0],
            'Especiales': Category.objects.get_or_create(name='Especiales', defaults={'order': 2})[0],
            'Temporada':  Category.objects.get_or_create(name='Temporada',  defaults={'order': 3})[0],
            'Cajas':      Category.objects.get_or_create(name='Cajas',      defaults={'order': 4})[0],
        }
        self.stdout.write(f'  ✓ Categorías: {len(cats)} listas')

        # ── Productos demo ────────────────────────────────────
        # (nombre, cat, descripción, precio, is_featured, status)
        demo_products = [
            (
                'Choco Chip Clásica',
                'Clásicas',
                'La galleta de toda la vida: crujiente por fuera, suave por dentro y cargada de chispas de chocolate. La que nunca traiciona.',
                '35.00',
                True,
                Product.Status.AVAILABLE,
            ),
            (
                'Brownie Cookie',
                'Especiales',
                'Galleta intensa con alma de brownie. Chocolate oscuro en cada mordida. Peligrosamente adictiva.',
                '45.00',
                True,
                Product.Status.AVAILABLE,
            ),
            (
                'Red Velvet',
                'Especiales',
                'Suavecita, bonita y con vibe de postre premium. La reina del menú en color rojo aterciopelado.',
                '45.00',
                True,
                Product.Status.AVAILABLE,
            ),
            (
                'Cookies & Cream',
                'Clásicas',
                'Trozos de galleta de crema en cada mordida. Para las que saben que lo mejor siempre va de dos en dos.',
                '40.00',
                False,
                Product.Status.AVAILABLE,
            ),
            (
                'Snickerdoodle',
                'Clásicas',
                'Canela y azúcar en la costra perfecta. Clásica estadounidense que ya ganó en Saltillo.',
                '35.00',
                False,
                Product.Status.AVAILABLE,
            ),
            (
                'Limón con Chía',
                'Temporada',
                'Frescura de limón con textura ligera. Solo por temporada. Cuando se acaba, se acaba.',
                '40.00',
                True,
                Product.Status.PREORDER,
            ),
            (
                'Matcha White Choco',
                'Especiales',
                'Matcha japonés con chips de chocolate blanco. Para los que saben de sabores y de vibes.',
                '50.00',
                False,
                Product.Status.SOLD_OUT,
            ),
            (
                'Caja Mix 6 piezas',
                'Cajas',
                'Surtido de 6 galletas de tu elección. Perfecto para regalar, compartir o fingir que vas a compartir.',
                '210.00',
                True,
                Product.Status.AVAILABLE,
            ),
            (
                'Caja Mix 12 piezas',
                'Cajas',
                'La caja grande para eventos, regalos o cuando el antojo no tiene freno. Surtido a tu gusto.',
                '390.00',
                False,
                Product.Status.AVAILABLE,
            ),
        ]

        created = 0
        for name, cat_name, desc, price, featured, status in demo_products:
            _, was_created = Product.objects.get_or_create(
                name=name,
                defaults={
                    'category': cats[cat_name],
                    'description': desc,
                    'price': Decimal(price),
                    'is_featured': featured,
                    'status': status,
                }
            )
            created += int(was_created)

        self.stdout.write(f'  ✓ Productos: {created} nuevos creados (total configurado: {len(demo_products)})')

        # ── Promociones demo ──────────────────────────────────
        promos = [
            (
                '2x1 en Clásicas — Jueves',
                'Cada jueves: compra dos Choco Chip o Snickerdoodle y paga solo una. Válido coordinando por WhatsApp.',
            ),
            (
                'Giveaway Instagram',
                'Espacio listo para tu próxima dinámica: sigue la cuenta, etiqueta a una amiga y gana una caja mix. Actívalo desde el admin.',
            ),
            (
                'Pedidos para eventos universitarios',
                'Mercaditos, bazares, reuniones de facultad. Pide con anticipación y coordinamos volumen y entrega.',
            ),
        ]

        promo_count = 0
        for title, desc in promos:
            _, was_created = Promotion.objects.get_or_create(
                title=title,
                defaults={'description': desc, 'is_active': True}
            )
            promo_count += int(was_created)

        self.stdout.write(f'  ✓ Promociones: {promo_count} nuevas creadas')

        # ── Resumen final ─────────────────────────────────────
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('¡Demo lista! Ahora corre:'))
        self.stdout.write('  python manage.py createsuperuser')
        self.stdout.write('  python manage.py runserver')
        self.stdout.write('')
        self.stdout.write(self.style.WARNING(
            'WhatsApp configurado: 528443108356 (844 310 8356)\n'
            'Instagram: https://www.instagram.com/coookieslab/\n'
            'URLs: / | /menu/ | /promos/ | /pedido/ | /admin/'
        ))
