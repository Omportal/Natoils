from django.db import models



class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    img = models.ImageField(verbose_name='Фотография')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name