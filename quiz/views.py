from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import quizzes, questions, choices, categories

# Create your views here.
#get all categories from the categories model
def get_category_set(request):
    try:
        category = categories.objects.all()
    except categories.DoesNotExist:
        raise Http404("No categories found")
    #prepare a list of categories to send as json
    category_set = list(category.values("category_id", "category_name"))
    return JsonResponse({"category_set": category_set})

#get all quizzes from the quizzes model of a category
def get_quizzes_set(request, category_id):
    try:
        category = categories.objects.get(category_id=category_id) #get the categorywith the given category_id
        quizzes_set = category.quizzes_set.all() #get all quizzes in the category as querySet
    except category.DoesNotExist:
        raise Http404("Category does not exist")
    #prepare a list of quizzes to send as json
    quizzes_set = list(quizzes_set.values("quiz_id" ,"title", "pub_date"))
    return JsonResponse({"quizzes_set": quizzes_set})

#Get all questions from the questions model of a quiz
def get_question_set(request, quiz_id):
    try:
        quiz = quizzes.objects.get(pk=quiz_id) #get the quiz with the given quiz_id
        question_set = quiz.questions_set.all() #get all questions in the quiz as querySet
    except quizzes.DoesNotExist:
        raise Http404("Quiz does not exist")
    #prepare a list of questions to send as json
    question_set = list(question_set.values("question_id", "question_text"))  #list converts it to s list of dictionaries
    return JsonResponse({"question_set": question_set})

#Get all choices from the choices model of a question
def get_choices_set(request, question_id):
    try:
        question = questions.objects.get(pk=question_id) #get the question with the given question_id
        choices_set = question.choices_set.all() #get all choices of the question as querySet
    except questions.DoesNotExist:
        raise Http404("Question does not exist")
    #prepare a list of questions to send as json
    choices_set = list(choices_set.values("choice_text", "is_correct_choice"))  #list converts it to s list of dictionaries
    return JsonResponse({"choices_set": choices_set})
