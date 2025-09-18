from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Главная'

@app.route('/personal_account')
def personal_account():
    return 'Личный кабинет'

@app.route('/personal_account/bonuses_and_promotions')
def bonuses_and_promotions():
    return 'Бонусы и акции'

@app.route('/personal_account/reviews')
def reviews():
    return 'Отзывы'

@app.route('/about us')
def about_us():
    return 'О нас'

@app.route('/about us/team')
def team():
    return 'Команда'

@app.route('/about us/company story')
def company_story():
    return 'История компании'

@app.route('/contacts')
def contacts():
    return 'Контакты'

@app.route('/contacts/phone number')
def phone_number():
    return 'Телефон'

@app.route('/contacts/email')
def email():
    return 'email'

@app.route('/contacts/social media')
def social_media():
    return 'соцсети'

@app.route('/clothes')
def clothes():
    return 'Одежда'

@app.route('/clothes/outerwear')
def outerwear():
    return 'Верхняя одежда'

@app.route('/clothes/outerwear/jackets')
def jackets():
    return 'Куртки'

@app.route('/clothes/outerwear/coats')
def coats():
    return 'Пальто'

@app.route('/clothes/outerwear/windbreakers')
def windbreakers():
    return 'Ветровки'

@app.route('/clothes/shoes')
def shoes():
    return 'Обвуь'

@app.route('/clothes/shoes/boots')
def boots():
    return 'Ботинки'

@app.route('/clothes/shoes/sneakers')
def sneakers():
    return 'Кроссовки'

@app.route('/clothes/accessories')
def accessories():
    return 'Аксессуары'

@app.route('/clothes/accessories/ties')
def ties():
    return 'Галстуки'

@app.route('/clothes/accessories/belts')
def belts():
    return 'Ремни'

@app.route('/clothes/accessories/gloves')
def gloves():
    return 'Перчатки'

if __name__ == '__main__':
    print ("Привет мир")
    app.run(debug=True)

#