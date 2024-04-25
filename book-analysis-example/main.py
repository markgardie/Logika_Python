from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
import io
import os
import json
import numpy as np

# відкриття книг та їх завантаження в словник
def open_books():

    # збір цікавих книг
    interesting_path = os.path.join(__file__, "..", "nikita/interesting")

    interesting = {}

    # відкриваємо папку з цікавими книгами
    interesting_files = os.listdir(interesting_path)


    # читаємо кожен файл і записуємо в словник
    for file in interesting_files:
        book_path = os.path.join(interesting_path, file)

        with io.open(book_path,  encoding='utf-8') as book:
            text = book.read()
            # Ставимо мітку, що книга є цікавою, список сентиментів поки пустий
            interesting[file] = {"interesting": True, "text": text, "sentiment": []}

    # не цікаві
    not_interesting_path = os.path.join(__file__, "..", "nikita/not_interesting")

    not_interesting = {}

    not_interesting_files = os.listdir(not_interesting_path)

    for file in not_interesting_files:
        book_path = os.path.join(not_interesting_path, file)

        with io.open(book_path,  encoding='utf-8') as book:
            text = book.read()
            # ставимо мітку, що книга не є цікавою
            not_interesting[file] = {"interesting": False, "text": text, "sentiment": []}

    # об'єднуємо два словники
    all_books = {**interesting, **not_interesting}

    # повертаємо результуючий словник
    return all_books

# сентимент-аналіз
def sentiment_analysis(books):

    # шлях до json-файлу, в який будемо записувати результат
    json_path = os.path.join(__file__, "..", "sentiments.json")

    # аналізатор сентиментів
    analyzer = SentimentIntensityAnalyzer()

    sentiments = {}

    # відкриваємо кожну книгу в словнику
    for book in books:
        text = books[book]["text"]

        # токенізуємо текст до рівня речень
        sentences = nltk.sent_tokenize(text)

        scores = []

        # для кожного речення отримуємо оцінки сентиментів
        for sentence in sentences:
            scores.append(analyzer.polarity_scores(sentence)["compound"])

        # для згладжування графіку використовуємо алгоритм DCT-II
        scores_dct = dct(scores, norm='ortho', type=2)
        scores_lpf = scores_dct.copy()
        # ставимо фільтр 10, але також його можна змінити на 5, аби подивитись тип сюжету
        scores_lpf[10:] = 0


        filtered_scores = idct(scores_lpf, norm='ortho')

        # нормалізований наративний час, 100% замість абсолютних значень речень
        normalized_narrative = 100

        # нормалізація часу, отримання 100 оцінок
        filtered_scores = np.interp(np.linspace(0, 1, normalized_narrative), np.linspace(0, 1, len(filtered_scores)), filtered_scores)

        # запис сентиментів в словник
        sentiments[book] = {"interesting": books[book]["interesting"], "sentiments": filtered_scores.tolist()}

    # збереження в json-файл
    with io.open (json_path, "w") as json_file:
        json.dump(sentiments, json_file)

# створення графіків
def create_plots():

    # шляхи до папок, куди будемо зберігати створені графіки
    interesting_path = os.path.join(__file__, "..", "nikita/interesting_plots")
    not_interesting_path =os.path.join(__file__, "..", "nikita/not_interesting_plots")

    # підгрузка датасету
    path = os.path.join(__file__, "..", "sentiments.json")
    with open(path, "r") as f:
        data = json.load(f)

    # проходимось по всім книжкам
    for book in data.keys():

        book_name = book.split(".")[0] # отримуємо тільки назву книги, відкидаючи формат txt
        book_format = book_name + ".jpg" # додаємо формат зображення, аби графік можна було зберегти в цьому форматі

        plt.plot(data[book]["sentiments"]) # створюємо графік сентиментів
        plt.title(book_name) # додаємо заголовок сюжету

        if data[book]["interesting"] == True:  
            path = os.path.join(interesting_path, book_format) # якщо книга є цікавою, то зберігаємо в папці для цікавих книг
        else:
            path = os.path.join(not_interesting_path, book_format) # якщо книга не є цікавоб, то зберігаємо в папці для нецікавих книг

        plt.savefig(path) # зберігаємо графік у вигляді зображення в папки
        plt.clf() # очищаємо графік для наступних книг

books = open_books()
sentiment_analysis(books)
create_plots()