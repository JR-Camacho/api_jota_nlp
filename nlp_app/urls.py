from django.urls import path, include

from rest_framework import routers

from nlp_app import views

#Routes
router = routers.DefaultRouter()
router.register(r'sentiment-analysis-es', views.SentimentAnalysisEsViewSet, basename='sentiment-analysis-es')
router.register(r'sentiment-analysis-en', views.SentimentAnalysisEnViewSet, basename='sentiment-analysis-en')

urlpatterns = [
    path('', include(router.urls))
]
