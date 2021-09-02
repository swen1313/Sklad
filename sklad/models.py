from django.db import models

units_pieces = [
    ('piece', 'штука'),
    ('kilo', 'килограмм'),
    ('litr', 'литр')
]


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    qty = models.PositiveIntegerField(verbose_name='количество')
    price = models.PositiveIntegerField(verbose_name='цена')
    date_of_upload = models.DateTimeField(verbose_name='date', auto_now=True)
    units = models.CharField(choices=units_pieces, default='piece', max_length=10, verbose_name='единица')

    def __str__(self):
        return self.name


color = [
    ('red', 'красный'),
    ('blue', 'синий'),
    ('green', 'зеленый')
]


class Sklad(models.Model):
    name = models.CharField(max_length=200, verbose_name='краска')
    qty = models.IntegerField(verbose_name='количество коробок')
    color = models.CharField(choices=color, default='red', max_length=10, verbose_name='цвет')
    price = models.PositiveIntegerField(verbose_name='цена')
    date_of_upload = models.DateTimeField(verbose_name='date', auto_now=True)

    def __str__(self):
        return self.name