from django.shortcuts import render, redirect

from . models import Chapter, Exercise
from . forms import ChapterForm, ExerciseForm

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


def generate_chapter_list(chapter_name):
    chapter_list = []
    if chapter_name == "":
        chapter = Chapter()
    for c in Chapter.objects.all():
        chapter_list.append(c)
        if c.name == chapter_name:
            chapter = list(Chapter.objects.filter(name=chapter_name))[0]
    return [chapter_list, chapter]


def edit_chapter(request, chapter_name=""):
    context = {}
    [chapter_list, chapter] = generate_chapter_list(chapter_name)
    chapter_form = ChapterForm()
    if chapter_name!="":
        chapter_form=ChapterForm(instance=chapter)
    if request.method == 'POST':
        chapter_form = ChapterForm(request.POST)
        if chapter_form.is_valid():
            chapter.name = chapter_form.cleaned_data['name']
            chapter.displayName = chapter_form.cleaned_data['displayName']
            chapter.content = chapter_form.cleaned_data['content']
            if 'submit_chapter' in request.POST:
                chapter.save()
            elif 'delete_chapter' in request.POST:
                chapter.delete()
            return redirect("/tutorial/edit_chapters/")
    context['chapter_list'] = chapter_list
    context['chapterForm'] = chapter_form
    context['showExercise'] = (chapter_name!="")
    context['chapterName']=chapter_name
    return render(request, "edit_chapter/edit_chapter.html", context)


def edit_exercise(request, chapter_name, exercise_name=""):
    context = {}
    [chapter_list, chapter] = generate_chapter_list(chapter_name)
    exercise = Exercise()
    exercise_list=[]
    exercise=Exercise()
    for e in Exercise.objects.filter(chapter=chapter):
        exercise_list.append(e)
        if e.title==exercise_name:
            exercise=e
    exercise_form = ExerciseForm()
    if exercise_name!="":
        exercise_form=ExerciseForm(instance=exercise)
    if request.method == 'POST':
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            exercise.title = exercise_form.cleaned_data['title']
            exercise.description = exercise_form.cleaned_data['description']
            exercise.chapter = chapter
            exercise.save()
            if 'submit_exercise' in request.POST:
                exercise.save()
            if 'delete_exercise' in request.POST:
                exercise.delete()
            return redirect("/tutorial/edit_chapters/"+chapter_name)
    context['chapter_list'] = chapter_list
    context['exerciseForm'] = exercise_form
    context['showExercise'] = True
    context['chapterName']=chapter_name
    context['exercise_list'] =exercise_list
    return render(request, "edit_chapter/edit_exercise.html", context)
