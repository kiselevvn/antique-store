from django.db import models
from django.utils.translation import gettext as _


class NameMixin(models.Model):
    """
    Name Mixin;
    Contain 'name' field;
    Содержит поле 'Имя'
    """

    name = models.CharField(
        verbose_name=_("Name"), max_length=125, blank=True, null=True
    )

    class Meta:
        abstract = True


class ShortNameMixin(models.Model):
    """
     Short Name Mixin;
    Contain 'short_name' field;
    Содержит поле 'short_name' - (Краткое Имя)
    """

    short_name = models.CharField(
        verbose_name=_("Name"), max_length=125, blank=True, null=True
    )

    class Meta:
        abstract = True


class DescriptionMixin(models.Model):
    """
    Description Mixin;
    Contain 'description' field;
    Содержит поле 'description' - (Описание)
    """

    description = models.TextField(
        verbose_name=_("Description"), blank=True, null=True
    )

    class Meta:
        abstract = True


class OrderMixin(models.Model):
    """
    Order Mixin;
    Contains 'order' field;
    Содержит поле 'order' - (Сортировка)
    """

    order = models.PositiveIntegerField(verbose_name=_("Order"), default=0)

    class Meta:
        abstract = True


class DateCreatedMixin(models.Model):
    """
    Date Created Mixin;
    Contains 'date_created' field;
    Содержит поле 'date_created' - (Дата Создания)
    """

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DateUpdatedMixin(models.Model):
    """
    Date Updated Mixin;
    Contains 'date_updated' field;
    Содержит поле 'date_updated' - (Дата последнего обновления)
    """

    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True