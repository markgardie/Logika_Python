from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
import io
import os
import json
import numpy as np

def open_books():

    interesting_path = os.path.join(__file__, "..", "nikita/interesting")

    interesting = {}

    interesting_files = os.listdir(interesting_path)


    for file in interesting_files:
        book_path = os.path.join(interesting_path, file)

        with io.open(book_path,  encoding='utf-8') as book:
            text = book.read()
            interesting[file] = {"interesting": True, "text": text, "sentiment": []}

    not_interesting_path = os.path.join(__file__, "..", "nikita/not_interesting")

    not_interesting = {}

    not_interesting_files = os.listdir(not_interesting_path)

    for file in not_interesting_files:
        book_path = os.path.join(not_interesting_path, file)

        with io.open(book_path,  encoding='utf-8') as book:
            text = book.read()
            not_interesting[file] = {"interesting": False, "text": text, "sentiment": []}

    all_books = {**interesting, **not_interesting}

    return all_books

def sentiment_analysis(books):

    json_path = os.path.join(__file__, "..", "sentiments.json")

    analyzer = SentimentIntensityAnalyzer()

    sentiments = {}

    for book in books:
        text = books[book]["text"]

        sentences = nltk.sent_tokenize(text)

        scores = []

        for sentence in sentences:
            scores.append(analyzer.polarity_scores(sentence)["compound"])

        # scores_dct = dct(scores, norm='ortho', type=2)
        # scores_lpf = scores_dct.copy()
       
        # scores_lpf[10:] = 0


        # filtered_scores = idct(scores_lpf, norm='ortho')

        # normalized_narrative = 100

        # filtered_scores = np.interp(np.linspace(0, 1, normalized_narrative), np.linspace(0, 1, len(filtered_scores)), filtered_scores)

        sentiments[book] = {"interesting": books[book]["interesting"], "sentiments": scores.tolist()}

    # збереження в json-файл
    with io.open (json_path, "w") as json_file:
        json.dump(sentiments, json_file)

def create_plots():

    interesting_path = os.path.join(__file__, "..", "nikita/interesting_plots")
    not_interesting_path =os.path.join(__file__, "..", "nikita/not_interesting_plots")

    path = os.path.join(__file__, "..", "sentiments.json")
    with open(path, "r") as f:
        data = json.load(f)

    for book in data.keys():

        book_name = book.split(".")[0] 
        book_format = book_name + ".jpg"

        plt.plot(data[book]["sentiments"]) 
        plt.title(book_name) 

        if data[book]["interesting"] == True:  
            path = os.path.join(interesting_path, book_format) 
        else:
            path = os.path.join(not_interesting_path, book_format) 

        plt.savefig(path) 
        plt.clf()

books = open_books()
sentiment_analysis(books)
create_plots()