from django.db import models
from django.utils.translation import gettext as _


class OrderPosition(models.Model):
    """
    Позиция заказа
    """

    order = models.ForeignKey(
        "orders.Order", verbose_name=_("Заказ"), on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product", verbose_name=_("Товар"), on_delete=models.PROTECT
    )
    count = models.PositiveIntegerField(_("Количество"))

    class Meta:
        verbose_name = _("Позиция заказа")
        verbose_name_plural = _("Позиции заказа")

    def __str__(self):
        return f"{self.product} (кол-во {self.count})"
