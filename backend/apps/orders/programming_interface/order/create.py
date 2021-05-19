from rest_framework.generics import CreateAPIView
from rest_framework.serializers import ModelSerializer
from ...models import Order, OrderPosition
from ...service import OrderToWarehouse, OrderInstanceMutate
from apps.warehouse.models import OperationPosition, Operation


class OrderPositionSerializer(ModelSerializer):
    class Meta:
        model = OrderPosition
        fields = ["count", "product"]


class OrderSerializer(ModelSerializer):
    positions = OrderPositionSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "address",
            "comment",
            "positions",
        ]

    def create(self, validated_data):
        positions = validated_data.pop("positions")
        order = Order.objects.create(**validated_data)
        for position in positions:
            OrderPosition.objects.create(order=order, **position)
        #
        service_mutate = OrderInstanceMutate()
        order = service_mutate.execute(order)
        #
        service = OrderToWarehouse()
        service.execute(order, Operation, OperationPosition)
        return order


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
