class OrderToWarehouse:
    def create_warehouse_positions(
        self, order, operation, operation_position_model
    ):
        """
        Order position to
        warehouse operation positions
        """
        operation_positions = []
        for position in order.positions.all():
            operation_positions.append(
                operation_position_model(
                    operation=operation,
                    product=position.product,
                    count=position.count,
                )
            )
        return operation_positions

    def create_warehouse_comment(self, order):
        """
        Order fields to
        warehouse operation comment
        """
        comment = None
        comment = (
            f"{order.name}\n"
            + f"{order.address}\n"
            + f"{order.phone}\n"
            + f"{order.email}\n"
            + f"{order.comment}"
        )
        return comment

    def execute(
        self,
        order_instance,
        operation_model,
        operation_position_model,
    ):
        """ Main service function """

        # create comment
        comment = self.create_warehouse_comment(order_instance)

        # create positions list
        operation = operation_model.objects.create(comment=comment)

        # create operation in database
        operation.save()

        # create positions list
        positions = self.create_warehouse_positions(
            order_instance, operation, operation_position_model
        )

        # create positions in database
        operation_position_model.objects.bulk_create(positions)
