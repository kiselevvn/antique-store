from django.db.models import F


class UpdateCountProduct:
    """
    Обновление количества товаров
    """

    def execute(self, operation_position):

        operation_position.product.count = (
            F("count") + operation_position.count
        )
        operation_position.product.save()
        # for position in operation.positions.all():
        #     print(position)
