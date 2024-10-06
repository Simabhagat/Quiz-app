from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path("categories/", views.get_category_set, name="get_category_set"),
    path("<int:category_id>/quizzes/", views.get_quizzes_set, name="get_quizzes_set"),
    path("<int:quiz_id>/questions/", views.get_question_set, name="get_question_set"),
    path("<int:question_id>/choices/", views.get_choices_set, name="get_choices_set"),
]
