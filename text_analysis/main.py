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

    path = r"C:\Users\Марк\Desktop\Logika_Python\text_analysis\good_movies\Shrek.txt"

    text = ""

    with io.open(path, "r") as file:
        text = file.read()

    sentences = nltk.sent_tokenize(text)

    sentiment_analyzer = SentimentIntensityAnalyzer()

    scores = []

    for sentence in sentences:
        score = sentiment_analyzer.polarity_scores(sentence)["compound"]
        scores.append(score)