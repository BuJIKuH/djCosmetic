from django.db import models


class ProductsModel(models.Model):
    """Таблица с продукцией (товаров)"""
    name = models.CharField('Название', max_length=150)
    description = models.TextField('Описание', max_length=5000)
    image = models.ImageField('Картинка', upload_to='prod/%Y/%m/%d')
    consist = models.TextField('Состав', max_length=300)
    price = models.PositiveIntegerField('Цена')
    available = models.BooleanField(default=True)
    line = models.ForeignKey('CategoryLineModels', on_delete=models.CASCADE)
    slug = models.SlugField('Слаг', max_length=150, blank=True)

    def __str__(self):
        return f'{self.name} - {self.line}'

    class Meta:
        verbose_name = 'Косметика'
        verbose_name_plural = 'Косметика'


class CategoryLineModels(models.Model):
    """Таблица категории (линия косметики)"""
    name = models.CharField('Название', max_length=150)
    description = models.TextField('Описание', max_length=5000)
    slug = models.SlugField('Слаг', max_length=150, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Косметическая линия'
        verbose_name_plural = 'Косметические линии'
