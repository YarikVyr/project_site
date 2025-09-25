# API спецификация

## Публичные страницы HTML

*   GET/ - главная страница
*   POST/order_form/<sku> - страница оформления заявки на товар
*   GET/order/confirmation - страница с благодарностью за заказ

## JSON API

GET/api/products - список товаров

```
<h3 class="font-semibold text-lg">{{ item.get('clothes name') }}</h3>
                <p class="text-gray-600 mb-4">{{ item.get('price', 'N/A') }} ₽</p>
```

POST/api/orders - офррмление заявки на товар

```
<label for="name" class="block text-sm font-medium text-gray-700">Ваше имя:</label>
<label for="phone" class="block text-sm font-medium text-gray-700">Номер телефона:</label>
```

## Статусы и ошибки

Ошибка 404 - страница не найдена