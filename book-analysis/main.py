from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
import io
import os
import json
import numpy as np


folder_path = r""

def open_books():
    books = {}

    filenames = os.listdir(folder_path)

    for file in filenames:
        book_path = os.path.join(folder_path, file)
        with open(book_path, encoding="utf-8") as book:
            text = book.read()
            books[file] = {"text": text, "sentiments": []}

    return books

def sentiment_analysis(books):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = {}
    json_path = os.path.join(folder_path, "sentiments.json")

    for book in books:
        text = books[book]["text"]
        sentences = nltk.sent_tokenize(text)
        scores = []

        for sent in sentences:
            score = analyzer.polarity_scores(sent)["compound"]
            scores.append(score)

        scores_dct = dct(scores, norm='ortho', type=2)
        scores_lpf = scores_dct.copy()
       
        scores_lpf[10:] = 0


        filtered_scores = idct(scores_lpf, norm='ortho')

        normalized_narrative = 100

        filtered_scores = np.interp(np.linspace(0, 1, normalized_narrative), np.linspace(0, 1, len(filtered_scores)), filtered_scores)

        sentiments[book] = {"sentiments": filtered_scores.tolist()}

    with open(json_path, encoding="utf-8") as json_file:
        json.dump(sentiments, json_file)


def analyze_one_book():
    book_path = r"book-analysis\matrix.txt"

    with open(book_path, encoding="utf-8") as book_file:
        text = book_file.read()

    sentences = nltk.sent_tokenize(text)
    scores = []
    analyzer = SentimentIntensityAnalyzer()

    for sent in sentences:
        sentiment = analyzer.polarity_scores(sent)["compound"]
        scores.append(sentiment)
    
    scores_dct = dct(scores, norm='ortho', type=2)
    scores_lpf = scores_dct.copy()
       
    scores_lpf[5:] = 0


    filtered_scores = idct(scores_lpf, norm='ortho')

    normalized_narrative = 100

    filtered_scores = np.interp(np.linspace(0, 1, normalized_narrative), np.linspace(0, 1, len(filtered_scores)), filtered_scores)


    plt.plot(filtered_scores)
    plt.title("Example Book")
    plt.show()

analyze_one_book()