import numpy as np
import tensorflow as tf
import joblib
import os

# Load the tokenizers
TOKENIZER_ES_PATH = os.path.join(os.path.dirname(
    __file__), '..', 'imports/sentiment_analysis/spanish/tokenizers', 'tokenizer.pkl')
tokenizer_es = joblib.load(TOKENIZER_ES_PATH)

TOKENIZER_EN_PATH = os.path.join(os.path.dirname(
    __file__), '..', 'imports/sentiment_analysis/english/tokenizers', 'tokenizer.pkl')
tokenizer_en = joblib.load(TOKENIZER_EN_PATH)

# Load the models
MODEL_ES_PATH = os.path.join(os.path.dirname(
    __file__), '..', 'imports/sentiment_analysis/spanish/models', 'sentiment_analysis_spanish.h5')
model_es = tf.keras.models.load_model(MODEL_ES_PATH)

MODEL_EN_PATH = os.path.join(os.path.dirname(
    __file__), '..', 'imports/sentiment_analysis/english/models', 'sentiment_analysis.h5')
model_en = tf.keras.models.load_model(MODEL_EN_PATH)

# Make Spanish sentiment prediction
def make_es_prediction(text):
    return model_es.predict(np.array([tokenizer_es.encode(text)]))

# Make English sentiment prediction
def make_en_prediction(text):
    return model_en.predict(np.array([tokenizer_en.encode(text)]))