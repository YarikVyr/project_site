# Установка и запуск

## Предпосылки

*   Python 3.10+
*   Windows

## Локальный запуск

pip install flask
pip install sqlite3

##  Структура проекта

app/
├── app.py            
├── my_database.bd         
├── templates/                 
    └── base.html          
         index.html             
     clothes.html                   
       └── category_page.html                      
     order_form.html                
       └── order_confirmation.html 
     about_us.html                  
     contacts.html                                       

## app.py

```
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()

category_map = {
    'outwear': 'Верхняя одежда',
    'shoes': 'Обувь',
    'accessories': 'Аксессуары'
}
def get_products_by_category(category):
    # Преобразуем название из URL в название, используемое в базе данных
    db_category = category_map.get(category, category)
    cursor.execute("SELECT id, `clothes name`, `clothes description`, `price`, `image link`, `quantity`, `order link` FROM ER WHERE category = ?", (db_category,))
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def productDB():
    cursor.execute('SELECT id, `clothes name`, `clothes description`, `price`, `image link`, `quantity`, `order link` FROM ER')
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

@app.route('/')
def index():
    shop = productDB()
    return render_template("index.html", shop = shop)

@app.route('/clothes/<category>')
def show_category(category):
    # Get the Russian category name from the dictionary
    russian_category = category_map.get(category, category)
    products = get_products_by_category(russian_category)
    return render_template("category_page.html", shop = products, category = russian_category)

@app.route('/clothes')
def clothes():
    return render_template("clothes.html")

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

@app.route('/order_form/<int:product_id>')
def show_order_form(product_id):
    return render_template('order_form.html', product_id = product_id)

@app.route('/order/confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

@app.route('/user/<username>')
def user_profile(username):
    return render_template('index.html', name = username)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    print("Сервер запущен")
    app.run(debug=True)
```

## Переменные окружения

*   app - создание фабрики сайта
*   connection - подключение к базе данных
*   cursor - обработка значений из юазы данных 
*   category_map - обработка товаров по категориям
*   db_category - категория в базе данных 
*   columns - колонки
*   shop - база данных
*   category - категория
*   products - товары
*   methods - метод для заявки
*   product_id - id клиента
*   name - имя клиента
*   phone - телефон клиента
