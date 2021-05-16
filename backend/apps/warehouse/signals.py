from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OperationPosition
from .service import UpdateCountProduct


@receiver(post_save, sender=OperationPosition)
def update_count_product(sender, instance, created, **kwargs):
    if created:
        service = UpdateCountProduct()
        service.execute(instance)
