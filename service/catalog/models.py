from django.db import models


class Mark(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return f'{self.name}'


class Model(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='mark')
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return f'{self.name}'
