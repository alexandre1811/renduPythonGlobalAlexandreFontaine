from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['text']


admin.site.register(Question)
