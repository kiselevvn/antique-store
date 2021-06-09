## Описание освноных модулей приложения ##

Пользователи

1. Модель пользователя [октрыть код](https://github.com/kiselevvn/legal-service/blob/main/backend/apps/users/models.py)

Заказы

1. Модель "Заказ" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/orders/models/order.py)
1. Модель "Позиция позиция заказа" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/orders/models/order_position.py)
1. Сервис "Создания записи на складе, при добавлении заказа" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/orders/service/order_to_warehouse.py)
1. API Создания заказа [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/orders/programming_interface/order/create.py)

Товары

1. Модель "Картинка" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/products/models/picture.py)
1. Модель "Категория" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/products/models/category.py)
1. Модель "Товар" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/products/models/product.py)
1. Модель "Тег" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/products/models/tag.py)
1. Страница одного товара [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/products/views/product_detail.py)
1. Страница списка товаров [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/products/views/product_list.py)
1. API иформация об одном товаре [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/products/programming_interface/product/retrive.py)

Склад

1. Модель "Операция движения товара складе" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/orders/programming_interface/order/create.py)
1. Модель "Позиция операции движения товара на складе" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/warehouse/models/operation_position.py)
1. Сервис "Обновление количества товаров" [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/warehouse/service/update_count_product.py)
1. Реализация сервиса обновления количества товара через сигнал (используется при редактировании операций в админке) [октрыть код](https://github.com/kiselevvn/antique-store/blob/main/backend/apps/warehouse/signals.py)
