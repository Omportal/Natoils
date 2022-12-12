from django.db import models
from apps.product_app.models import Product
from apps.user_app.models import CustomUser
# Create your models here.



class Order(models.Model):
    """Модель заказа"""
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Клиент', related_name='order')
    product = models.ForeignKey(Product, related_name='order', verbose_name='Товар')
    count = models.PositiveIntegerField(verbose_name='Количество товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость заказа')

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'

    def __str__(self) -> str:
        return f"Клиент: {self.client},  продукт: {self.product}, цена: {self.price * self.count}"

    @property
    def get_total_price(self):
        return self.count * self.price