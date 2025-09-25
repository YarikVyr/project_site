# Тестирование

## Инструмент 

*   pytest

## Установка

```
pip install -U pytest
```
## Структура

tests/
├── get_products_by_category_test.py
├── productDB_test.py
├── index_test.py
├── show_category_test.py
├── clothes_test.py
├── handle_order_test.py
├── show_order_form_test.py
├── order_confirmation_test.py
├── user_profile_test.py
├── about_us_test.py
└── contacts_test.py

# Пример теста

```
from app import get_products_by_category
from app import cursor
from app import connection
from app import category_map

def get_products_by_category(category):
    db_category = category_map.get(category, category)
    cursor.execute("SELECT id, `clothes name`, `clothes description`, `price`, `image link`, `quantity`, `order link` FROM ER WHERE category = ?", (db_category,))
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
```
# Запуск теста

python -m pytest