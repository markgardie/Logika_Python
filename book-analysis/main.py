from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
import io
import os
import json
import numpy as np

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
       
    scores_lpf[10:] = 0


    filtered_scores = idct(scores_lpf, norm='ortho')

    normalized_narrative = 100

    filtered_scores = np.interp(np.linspace(0, 1, normalized_narrative), np.linspace(0, 1, len(filtered_scores)), filtered_scores)


    plt.plot(filtered_scores)
    plt.title("Example Book")
    plt.show()

analyze_one_book()