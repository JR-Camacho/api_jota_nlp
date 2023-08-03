from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .services.sentiment_analysis_service import make_es_prediction, make_en_prediction

# Create your views here.

#Sentiment Analysis Spanish ViewSet
class SentimentAnalysisEsViewSet(viewsets.ViewSet):

    def create(self, request):
        text = request.data.get("text")

        try:
            return Response({
                "prediction": make_es_prediction(text=text)
            })
        except Exception as e:
            error_message = str(e)
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#Sentiment Analysis English ViewSet
class SentimentAnalysisEnViewSet(viewsets.ViewSet):

    def create(self, request):
        text = request.data.get("text")

        try:
            return Response({
                "prediction": make_en_prediction(text=text)[0]
            })
        except Exception as e:
            error_message = str(e)
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
