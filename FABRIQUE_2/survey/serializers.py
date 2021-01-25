from rest_framework import serializers
from .models import *
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer



class SurveySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='surveys-detail')
    class Meta:
        model = Survey
        #fields = '__all__'
        fields = ('id', 'survey_name', 'url', 'pub_date', 'end_date', 'survey_description')

class QuestionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='questions-detail')
    class Meta:
        model = Question
        # fields = '__all__'
        fields = ('id', 'url', 'survey', 'question_type', 'question_text')

class ChoiceSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='choices-detail')
    class Meta:
        model = Choice
        #fields = '__all__'
        fields = ('id', 'url', 'choice_type')


class AnswerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='answers-detail')

    class Meta:
        model = Answer
        #fields = '__all__'
        fields = ('id', 'user_id', 'survey', 'url', 'question', 'choice', 'answer_text')





