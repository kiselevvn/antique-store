class ServiceBase:
    """
    Ovveride "execute()" method to use
    """

    def execute(self, *args, **kwargs):
        return super().execute(*args, **kwargs)
