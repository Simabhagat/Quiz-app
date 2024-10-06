from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import quizzes, questions, choices, categories

# Create your views here.

#Get all questions from the quiz model
def get_question_set(request, quiz_id):
    try:
        quiz = quizzes.objects.get(pk=quiz_id) #get the quiz with the given quiz_id
        question_set = quiz.questions_set.all() #get all questions in the quiz as querySet
    except quizzes.DoesNotExist:
        raise Http404("Quiz does not exist")
    #prepare a list of questions to send as json
    question_set = list(question_set.values("question_id", "question_text"))  #list converts it to s list of dictionaries
    return JsonResponse({"question_set": question_set})

#get all quizzes from a category model
def get_quizzes_set(request, category_id):
    try:
        category = categories.objects.get(category_id=category_id) #get the categorywith the given category_id
        quizzes_set = category.quizzes_set.all() #get all quizzes in the category as querySet
    except category.DoesNotExist:
        raise Http404("Category does not exist")
    #prepare a list of quizzes to send as json
    quizzes_set = list(quizzes_set.values("quiz_id" ,"title", "pub_date"))
    return JsonResponse({"quizzes_set": quizzes_set})

#get all categories from the category model
def get_category_set(request):
    try:
        category = categories.objects.all()
    except categories.DoesNotExist:
        raise Http404("No categories found")
    #prepare a list of categories to send as json
    category_set = list(category.values("category_id", "category_name"))
    return JsonResponse({"category_set": category_set})