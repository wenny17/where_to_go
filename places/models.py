from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    description_short = models.CharField(verbose_name="Краткое описание", max_length=200, blank=True)
    description_long = models.TextField(verbose_name="Описание", blank=True)
    lat = models.DecimalField(verbose_name="Широта", max_digits=10, decimal_places=8)
    lng = models.DecimalField(verbose_name="Долгота", max_digits=11, decimal_places=8)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title