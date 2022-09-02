from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Form for Topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Form for Entry"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
