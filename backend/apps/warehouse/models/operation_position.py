from django.db import models
from django.utils.translation import gettext as _


class OperationPosition(models.Model):
    """
    Позиция операции движения
    товара на складе
    """

    operation = models.ForeignKey(
        "warehouse.Operation",
        verbose_name=_("Заказ"),
        on_delete=models.CASCADE,
        related_name="positions",
    )
    product = models.ForeignKey(
        "products.Product",
        verbose_name=_("Товар"),
        on_delete=models.PROTECT,
    )
    count = models.IntegerField(_("Количество"), default=0)

    class Meta:
        verbose_name = _("Позиция операция")
        verbose_name_plural = _("Позиции операции")

    # def __str__(self):
    #     return f"{self.name} - {self.email} на сумму {self.price}"
