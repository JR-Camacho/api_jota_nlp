from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .services.sentiment_analysis_service import make_es_prediction, make_en_prediction
from .utils.process_text import extract_text_info, calculate_class_percentages

import numpy as np

# Create your views here.

# Sentiment Analysis Spanish ViewSet
class SentimentAnalysisEsViewSet(viewsets.ViewSet):

    def create(self, request):
        text = request.data.get("text")

        try:
            predictions = make_es_prediction(text=text.lower())
            return Response({
                "predictions": calculate_class_percentages(predictions[0]),
                "prediction": np.argmax(predictions[0]),
                "text_info": extract_text_info(text=text),
            })
        except Exception as e:
            error_message = str(e)
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Sentiment Analysis English ViewSet
class SentimentAnalysisEnViewSet(viewsets.ViewSet):

    def create(self, request):
        text = request.data.get("text")

        try:
            prediction = make_en_prediction(text=text.lower())[0][0]
            return Response({
                "prediction": round(prediction),
                "percentage": round(prediction * 100, 2),
                "text_info": extract_text_info(text=text),
            })
        except Exception as e:
            error_message = str(e)
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
