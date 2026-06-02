from decimal import Decimal
from django.core.management.base import BaseCommand
from apps.catalog.models import Category, Product
from apps.promos.models import Promotion
from apps.site_settings.models import BusinessSettings


class Command(BaseCommand):
    help = 'Crea datos demo para CookiesLab.'

    def handle(self, *args, **options):
        business = BusinessSettings.get_solo()
        business.business_name = 'CookiesLab'
        business.slogan = 'Galletitas que alegran tu día'
        business.hero_title = 'Cookies recién hechas para salvar tu antojo'
        business.hero_subtitle = 'De estudiantes para estudiantes. Elige tus favoritas y pide directo por WhatsApp.'
        business.location_text = 'Saltillo, Coahuila'
        business.delivery_notes = 'Entregas en puntos acordados, facultad y eventos/mercaditos según disponibilidad.'
        business.instagram_url = 'https://www.instagram.com/coookieslab/'
        business.save()

        categories = {
            'Clásicas': Category.objects.get_or_create(name='Clásicas', defaults={'order': 1})[0],
            'Especiales': Category.objects.get_or_create(name='Especiales', defaults={'order': 2})[0],
            'Temporada': Category.objects.get_or_create(name='Temporada', defaults={'order': 3})[0],
        }

        demo_products = [
            ('Choco Chip', 'Clásicas', 'La clásica que nunca traiciona: crujiente por fuera y suave por dentro.', '35.00', True),
            ('Brownie Cookie', 'Especiales', 'Galleta intensa con alma de brownie. Peligrosamente buena.', '45.00', True),
            ('Red Velvet', 'Especiales', 'Suavecita, bonita y con vibe de postre premium.', '45.00', True),
            ('Cookies & Cream', 'Clásicas', 'Trozos de galleta cremosa en cada mordida.', '40.00', False),
            ('Caja Mix 6', 'Temporada', 'Caja surtida para compartir, regalar o fingir que vas a compartir.', '210.00', True),
        ]

        created = 0
        for name, cat, description, price, featured in demo_products:
            _, was_created = Product.objects.get_or_create(
                name=name,
                defaults={
                    'category': categories[cat],
                    'description': description,
                    'price': Decimal(price),
                    'is_featured': featured,
                    'status': Product.Status.AVAILABLE,
                }
            )
            created += int(was_created)

        Promotion.objects.get_or_create(
            title='Promo de estudiantes',
            defaults={
                'description': 'Pregunta por paquetes para clases, mercaditos y eventos universitarios.',
                'is_active': True,
            }
        )
        Promotion.objects.get_or_create(
            title='Giveaway activo',
            defaults={
                'description': 'Espacio listo para dinámicas de Instagram, rifas o colaboraciones.',
                'is_active': True,
            }
        )

        self.stdout.write(self.style.SUCCESS(f'Demo lista. Productos nuevos: {created}.'))
        self.stdout.write(self.style.WARNING('Recuerda configurar el WhatsApp real en Admin > Configuración del negocio.'))
