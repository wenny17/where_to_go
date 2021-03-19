from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    description_short = models.TextField(verbose_name="Краткое описание", blank=True)
    description_long = HTMLField(verbose_name="Описание")
    lat = models.DecimalField(verbose_name="Широта", max_digits=10, decimal_places=8)
    lng = models.DecimalField(verbose_name="Долгота", max_digits=11, decimal_places=8)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='photos/')
    order = models.IntegerField('Позиция', default=0, blank=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f"{self.place}-{self.order}"
