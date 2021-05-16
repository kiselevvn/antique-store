from django.db import models
from django.utils.translation import gettext as _


class Tag(models.Model):
    """
    Тег товара
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=255)

    class Meta:
        verbose_name = _("Тег товара")
        verbose_name_plural = _("Теги товаров")

    def __str__(self):
        return self.name
