from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField('nombre', max_length=100)
    slug = models.SlugField('slug', max_length=120, unique=True, blank=True)
    description = models.TextField('descripción', blank=True)
    order = models.PositiveIntegerField('orden', default=0)
    is_active = models.BooleanField('activa', default=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'available', 'Disponible'
        PREORDER = 'preorder', 'Preventa'
        SOLD_OUT = 'sold_out', 'Agotado'
        HIDDEN = 'hidden', 'Oculto'

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name='categoría')
    name = models.CharField('nombre', max_length=120)
    slug = models.SlugField('slug', max_length=140, unique=True, blank=True)
    description = models.TextField('descripción', blank=True)
    price = models.DecimalField('precio', max_digits=10, decimal_places=2)
    image = models.ImageField('imagen', upload_to='product_images/', blank=True, null=True)
    status = models.CharField('estado', max_length=20, choices=Status.choices, default=Status.AVAILABLE)
    is_featured = models.BooleanField('destacado', default=False)
    created_at = models.DateTimeField('creado', auto_now_add=True)
    updated_at = models.DateTimeField('actualizado', auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['category__order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def is_orderable(self):
        return self.status in {self.Status.AVAILABLE, self.Status.PREORDER}

    def get_absolute_url(self):
        return reverse('catalog:menu') + f'#{self.slug}'
