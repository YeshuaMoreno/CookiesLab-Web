from django.db import models
from django.utils import timezone


class Promotion(models.Model):
    title = models.CharField('título', max_length=140)
    description = models.TextField('descripción', blank=True)
    image = models.ImageField('imagen', upload_to='promo_images/', blank=True, null=True)
    starts_at = models.DateTimeField('inicia', blank=True, null=True)
    ends_at = models.DateTimeField('termina', blank=True, null=True)
    is_active = models.BooleanField('activa', default=True)
    created_at = models.DateTimeField('creada', auto_now_add=True)

    class Meta:
        verbose_name = 'promoción'
        verbose_name_plural = 'promociones'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def is_current(self):
        now = timezone.now()
        if not self.is_active:
            return False
        if self.starts_at and self.starts_at > now:
            return False
        if self.ends_at and self.ends_at < now:
            return False
        return True
