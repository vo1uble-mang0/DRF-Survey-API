from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('surveys', SurveyViewSet, basename='surveys')
router.register('questions', QuestionViewSet, basename='questions')
router.register('choices', ChoiceViewSet, basename='choices')
router.register('answers', AnswerViewSet, basename='answers')
urlpatterns = router.urls

