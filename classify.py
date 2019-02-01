import os
from os import path

import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

import joblib

model = joblib.load("model/model_mlp.pkl")

DICTIONARY_PATH = os.getenv("DICTIONARY_PATH")
dictionary_exist = path.exists(DICTIONARY_PATH)
if (dictionary_exist):
    df = pd.read_csv(DICTIONARY_PATH)

def identify_language(kata):
    skor_indonesia = 0.1
    skor_inggris = 0.1

    if (dictionary_exist):
        search = df.loc[df['kata'].isin([kata.lower()])]
        if ('indonesia') in search.bahasa.values:
            skor_indonesia = 1
        if ('inggris') in search.bahasa.values:
            skor_inggris = 1

    skor_ngraph = model.predict_proba([kata.lower()])
    skor_indonesia = skor_indonesia * skor_ngraph[0][0]
    skor_inggris = skor_inggris * skor_ngraph[0][1]

    if (skor_indonesia >= skor_inggris):
        return "Indonesia"
    else:
        return "Inggris"
