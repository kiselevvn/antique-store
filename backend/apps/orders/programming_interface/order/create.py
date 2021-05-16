from rest_framework.generics import CreateAPIView
from rest_framework.serializers import ModelSerializer
from ...models import Order, OrderPosition


class OrderPositionSerializer(ModelSerializer):
    class Meta:
        model = OrderPosition
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    pictures = OrderPositionSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "name", "email", "phone", "address", "comment"]


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
