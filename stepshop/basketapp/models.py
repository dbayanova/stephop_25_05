from django.db import models
from mainapp.models import Product
from stepshop import settings


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
        verbose_name='корзина'
    )

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        default=0,
    )

    add_datetime = models.DateTimeField(
        verbose_name='Время',
        auto_now_add=True,
    )
