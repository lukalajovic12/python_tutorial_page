from django.db import models
from django.forms import ModelForm
from django import forms


class Chapter(models.Model):
    name = models.CharField(max_length=500, default="")
    displayName = models.CharField(max_length=500, default="")
    content = models.TextField(default="")

    def __str__(self):
        return "name: " + self.name + " " + "displayName:" + self.displayName


class ChapterForm(ModelForm):
    name = forms.CharField(label="name", required=True)
    displayName = forms.CharField(label="displayName", required=True)
    content = forms.CharField(label="content", required=True)

    class Meta:
        model = Chapter
        fields = ['name', 'displayName', 'content']


class Exercise(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "title: " + self.title + "\n" + "description: +\n" + self.description


class ExerciseForm(ModelForm):
    title = forms.CharField(label="name", required=True)
    description = forms.CharField(label="content", required=True)

    class Meta:
        model = Exercise
        fields = ['title', 'description']


