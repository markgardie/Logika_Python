from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
import io
import os
import json
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split


def analyze_one_file():

    path = r"C:\Users\Марк\Desktop\Logika_Python\text_analysis\Terminator Genisys.txt"

    text = ""

    with io.open(path, "r") as file:
        text = file.read()

    sentences = nltk.sent_tokenize(text)

    sentiment_analyzer = SentimentIntensityAnalyzer()

    scores = []

    for sentence in sentences:
        score = sentiment_analyzer.polarity_scores(sentence)["compound"]
        scores.append(score)

    
    scores_dct = dct(scores, norm = "ortho", type = 2)
    scores_dct[10:] = 0
    scores_filtered = idct(scores_dct, norm="ortho")

    narrative_time = 100

    scores_normalized = np.interp(np.linspace(0, 1, narrative_time), np.linspace(0, 1, len(scores_filtered)), scores_filtered)


    plt.plot(scores_normalized)
    plt.title("Terminator Genisys")
    plt.savefig(r"C:\Users\Марк\Desktop\Logika_Python\text_analysis\Terminator Genisys")


analyze_one_file()