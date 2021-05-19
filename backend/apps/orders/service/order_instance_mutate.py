class OrderInstanceMutate:
    def mutate_instance(self, instance):
        for position in instance.positions.all():
            position.count = -position.count
            position.save()
        return instance

    def execute(self, order_instance):
        """ Main service function """
        old_instance = order_instance

        mutate_instance = self.mutate_instance(old_instance)

        return mutate_instance
