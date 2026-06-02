from django.db import models


class BusinessSettings(models.Model):
    business_name = models.CharField('nombre del negocio', max_length=120, default='CookiesLab')
    slogan = models.CharField('slogan', max_length=180, default='Galletitas que alegran tu día')
    hero_title = models.CharField('título principal', max_length=180, default='Cookies recién hechas para salvar tu día')
    hero_subtitle = models.TextField('subtítulo principal', blank=True, default='De estudiantes para estudiantes. Pide por WhatsApp y coordina tu entrega.')
    whatsapp_number = models.CharField('WhatsApp', max_length=20, blank=True, help_text='Solo números, ejemplo: 528441234567')
    instagram_url = models.URLField('Instagram', blank=True, default='https://www.instagram.com/coookieslab/')
    location_text = models.CharField('ubicación', max_length=180, blank=True, default='Saltillo, Coahuila')
    delivery_notes = models.TextField('notas de entrega', blank=True, default='Entregas sujetas a disponibilidad. Coordina horario y punto por WhatsApp.')
    logo = models.ImageField('logo', upload_to='brand/', blank=True, null=True)
    is_active = models.BooleanField('activa', default=True)
    updated_at = models.DateTimeField('actualizado', auto_now=True)

    class Meta:
        verbose_name = 'configuración del negocio'
        verbose_name_plural = 'configuración del negocio'

    def __str__(self):
        return self.business_name

    def save(self, *args, **kwargs):
        if not self.pk and BusinessSettings.objects.exists():
            self.pk = BusinessSettings.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
