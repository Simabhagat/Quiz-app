from django.contrib import admin

# Register your models here.

from .models import users, categories, quizzes, questions, choices, quizAttempt 

admin.site.register(users)
admin.site.register(categories)
admin.site.register(quizzes)
admin.site.register(questions)
admin.site.register(choices)
admin.site.register(quizAttempt)
