'''
Created on 2018. 12. 22.

@author: user
'''
from django.forms.models import ModelForm
from .models import Question, Choice

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name']

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['q', 'name']