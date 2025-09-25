from app import get_products_by_category
from app import cursor
from app import connection
from app import category_map

def get_products_by_category(category):
    db_category = category_map.get(category, category)
    cursor.execute("SELECT id, `clothes name`, `clothes description`, `price`, `image link`, `quantity`, `order link` FROM ER WHERE category = ?", (db_category,))
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
