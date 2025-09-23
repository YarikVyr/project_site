import sqlite3
import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Подключение к базе данных
connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()

# Создаем таблицу для заявок
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        "client name" TEXT,
        "client number" TEXT,
        "comment" TEXT,
        product_id INTEGER
    )
''')
connection.commit()

# Словарь для перевода категорий из URL в названия в базе данных
category_map = {
    'outwear': 'Верхняя одежда',
    'shoes': 'Обувь',
    'accessories': 'Аксессуары'
}

# Функция для получения товаров по категории
def get_products_by_category(category):
    # Преобразуем название из URL в название, используемое в базе данных
    db_category = category_map.get(category, category)
    cursor.execute("SELECT id, `clothes name`, `clothes description`, `price`, `image link`, `quantity`, `order link` FROM ER WHERE category = ?", (db_category,))
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# Функция для получения всех товаров
def productDB():
    cursor.execute('SELECT id, `clothes name`, `clothes description`, `price`, `image link`, `quantity`, `order link` FROM ER')
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# Маршрут для главной страницы
@app.route('/')
def index():
    shop = productDB()
    return render_template("index.html", shop = shop)

# Маршрут для страницы категорий
@app.route('/clothes/<category>')
def show_category(category):
    products = get_products_by_category(category)
    category_name = category_map.get(category, 'Категория')
    return render_template("category_page.html", shop = products, category_name = category_name)

# Маршрут для страницы мужской одежды
@app.route('/clothes')
def clothes():
    return render_template("clothes.html")

# Обработка заявок
@app.route('/order', methods=['POST'])
def handle_order():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        name = request.form.get('name')
        phone = request.form.get('phone')
        
        cursor.execute(
            "INSERT INTO orders (`client name`, `client number`, `comment`, `product_id`) VALUES (?, ?, ?, ?)",
            (name, phone, 'Заявка на товар', product_id)
        )
        connection.commit()
        
        return redirect(url_for('order_confirmation'))

@app.route('/order/confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

@app.route('/user/<username>')
def user_profile(username):
    return render_template('index.html', name = username)

# Другие маршруты
@app.route('/about us')
def about_us():
    return 'О нас'

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    print("Сервер запущен")
    app.run(debug=True)
