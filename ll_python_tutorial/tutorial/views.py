from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from . import models

Chapter = models.Chapter
Exercise = models.Exercise
ChapterForm = models.ChapterForm


def read_chapters(request, chapter_name=""):
    context = {}
    chapter_list = []
    exercises = []
    title = ""
    content = ""
    for c in Chapter.objects.all():
        chapter_list.append(c)
    if chapter_name != "":
        current_chapter = list(Chapter.objects.filter(name=chapter_name))[0]
        title = current_chapter.displayName
        content = current_chapter.content
        for e in Exercise.objects.filter(chapter=current_chapter):
            exercises.append(e)
    context["title"] = title
    context['content'] = content
    context['chapter_list'] = chapter_list
    context["exercises"] = exercises
    return render(request, "read_chapters.html", context)


def new_chapter(request, chapter_name=""):
    context = {}
    chapter_list = []
    readonlyValue = ""
    if chapter_name == "":
        chapter = Chapter()
    for c in Chapter.objects.all():
        chapter_list.append(c)
        if c.name == chapter_name:
            chapter = list(Chapter.objects.filter(name=chapter_name))[0]
    if chapter_name != "":
        readonlyValue = "readOnly"
    if request.method == 'POST':
        chapter_form = ChapterForm(request.POST)
        if chapter_form.is_valid():
            chapter.name = chapter_form.cleaned_data['name']
            chapter.displayName = chapter_form.cleaned_data['displayName']
            chapter.content = chapter_form.cleaned_data['content']
            if 'submit' in request.POST:
                chapter.save()
                nameValue = chapter.name
                displayNameValue = chapter.displayName
                contentValue = chapter.content
                if chapter_name != "":
                    readonlyValue = "readOnly"
                    chapter_list.append(chapter)
            elif 'delete' in request.POST:
                chapter.delete()
    context['chapter'] = chapter
    context['readonlyValue'] = readonlyValue
    context['chapter_list']=chapter_list
    return render(request, "edit_chapter/edit_chapters.html", context)


class MyFormView(View):
    form_class = ChapterForm
    template_name = 'edit_chapter/edit_chapters.html'

    def get(self,request, chapter_name=""):
        context = {}
        chapter_list = []
        readonlyValue = ""
        if chapter_name == "":
            chapter = Chapter()
        for c in Chapter.objects.all():
            chapter_list.append(c)
            if c.name == chapter_name:
                chapter = list(Chapter.objects.filter(name=chapter_name))[0]
        if chapter_name != "":
            readonlyValue = "readOnly"


        return render(request, self.template_name, context)


    def post(self,request, chapter_name=""):
        context = {}
        readonlyValue = ""
        if chapter_name == "":
            chapter = Chapter()
        for c in Chapter.objects.all():
            if c.name == chapter_name:
                chapter = list(Chapter.objects.filter(name=chapter_name))[0]
        if chapter_name != "":
            readonlyValue = "readOnly"
        if request.method == 'POST':
            chapter_form = self.form_class(request.POST)
            if chapter_form.is_valid():
                chapter.name = chapter_form.cleaned_data['name']
                chapter.displayName = chapter_form.cleaned_data['displayName']
                chapter.content = chapter_form.cleaned_data['content']
                if 'submit' in request.POST:
                    chapter.save()
                    nameValue = chapter.name
                    displayNameValue = chapter.displayName
                    contentValue = chapter.content
                    if chapter_name != "":
                        readonlyValue = "readOnly"
                        chapter_list.append(chapter)
                elif 'delete' in request.POST:
                    chapter.delete()
        context['chapter'] = chapter
        context['readonlyValue'] = readonlyValue
        context['chapter_list']=chapter_list
        return render(request, self.template_name, context)
