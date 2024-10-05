from django.db import models

# Create your models here.

#user model --> quiz_users(table name)
#can be extended to add more fields
class users(models.Models):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField( max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

#categories model --> quiz_categories
class categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField("subject", max_length=50) #in admin panel, the field will be displayed as subject instead of category name


#quizes model --> quiz_quizes
class quizzes(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    title = models.CharField( max_length=20)  #will be a topic of a particular subject
    pub_date = models.DateTimeField("published date")
    category = models.ForeignKey(categories, on_delete=models.CASCADE)


#questions model --> quiz_questions
class questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    quiz = models.ForeignKey(quizzes, on_delete=models.CASCADE)
    
#choices model --> quiz_choices
class choices(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(questions, on_delete=models.CASCADE) #cascade deletes all objects that point to the reference object
                                                                    #in this case, delete all choices when the question is deleted
    is_correct_choice = models.BooleanField(default=False)  #marks if this is the correct choice

#category table(subjects) will have one to many relationship with quizzes table
#quizzes table will have one to many relationship with questions table
#questions table will have one to many relationship with choices table


class quizAttempt(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    quiz = models.ForeignKey(quizzes, on_delete=models.CASCADE)
    question = models.ForeignKey(questions, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(choices, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)


#check if choice is correct when user submits a choice to a question
# def submit_answer(user, quiz, question, selected_choice):
#     is_correct = selected_choice.is_correct_choice
#     QuizAttempt for logging when we want to add more features
#     QuizAttempt.objects.create(
#         user=user,
#         quiz=quiz,
#         question=question,
#         selected_choice=selected_choice,
#         is_correct=is_correct
#     )
#     return is_correct

#to get total number of correct answers for a user on a quiz
# correct_answers = QuizAttempt.objects.filter(user=user, quiz=quiz, is_correct=True).count()
