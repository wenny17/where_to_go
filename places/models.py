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


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='photos/')
    order = models.IntegerField('Позиция', default=0, blank=False, null=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f"{self.place}-{self.order}"
