from flask import Flask
import random
import os
import re
from datetime import datetime, timedelta

app = Flask(__name__)

# Глобальные переменные
car_list = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cat_breeds = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

# Загружаем текст книги и создаем список слов
with open(BOOK_FILE, encoding='utf-8') as book:
    text = book.read()
    words = re.findall(r'\b\w+\b', text)

# Счетчик для /counter
@app.route('/counter')
def counter():
    if not hasattr(counter, 'visits'):
        counter.visits = 0
    counter.visits += 1
    return f'Страница была открыта {counter.visits} раз(а).'

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def cars():
    return ', '.join(car_list)

@app.route('/cats')
def cats():
    return random.choice(cat_breeds)

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Точное время: {current_time}'

@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    return f'Точное время через час будет: {current_time_after_hour}'

@app.route('/get_random_word')
def get_random_word():
    random_word = random.choice(words)
    return random_word

if __name__ == '__main__':
    app.run(debug=True)
