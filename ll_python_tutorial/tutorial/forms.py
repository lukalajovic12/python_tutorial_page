
from django.forms import ModelForm
from django import forms

from . models import Exercise
from . models import Chapter


class ChapterForm(ModelForm):
    name = forms.CharField(label="name", required=True)
    displayName = forms.CharField(label="displayName", required=True)
    content = forms.CharField(label="content", required=True,widget=forms.Textarea(attrs={"rows":20, "cols":50}))

    class Meta:
        model = Chapter
        fields = ['name', 'displayName', 'content']





class ExerciseForm(ModelForm):
    title = forms.CharField(label="title", required=True)
    description = forms.CharField(label="description", required=True,widget=forms.Textarea(attrs={"rows":20, "cols":50}))

    class Meta:
        model = Exercise
        fields = ['title', 'description']


