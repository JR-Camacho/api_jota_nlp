import string
from langdetect import detect

def calculate_class_percentages(prediction_probabilities):
    total_prob = sum(prediction_probabilities)
    class_percentages = [{'class': i, 'total': prob, 'percentage': round(prob * 100 / total_prob, 2)} for i, prob in enumerate(prediction_probabilities)]
    return class_percentages

def extract_text_info(text):
    # Get the number of special characters
    special_characters = sum(1 for char in text if char in string.punctuation)

    # Detect the language of the text
    language = detect(text)

    text_info = {
        "special_characters": special_characters,
        "language": language,
    }

    return text_info