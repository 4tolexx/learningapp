from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('play/', views.play, name='play'),
    path('score/', views.score, name='score'),
    path('submission-result/<int:attempted_question_pk>/', views.submission_result, name='submission_result'),

]
