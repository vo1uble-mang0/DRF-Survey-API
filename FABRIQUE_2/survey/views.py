from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model


class SurveyViewSet(ModelViewSet):
    model = get_user_model()
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #http_method_names = ['get', 'post']


class QuestionViewSet(ModelViewSet):
    model = get_user_model()
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #http_method_names = ['get', 'post']
    #http_method_names = ['get']

class ChoiceViewSet(ModelViewSet):
    model = get_user_model()
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class AnswerViewSet(ModelViewSet):
    model = get_user_model()
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']



