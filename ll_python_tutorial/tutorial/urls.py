from django.urls import path

from . import views

urlpatterns = [
    path('read_chapters/<str:chapter_name>', views.read_chapters),
    path('read_chapters/', views.read_chapters),
    path('edit_chapters/<str:chapter_name>', views.edit_chapter),
    path('edit_chapters/', views.edit_chapter),
    path('edit_exercise/<str:chapter_name>', views.edit_exercise),
    path('edit_exercise/<str:chapter_name>/<str:exercise_name>', views.edit_exercise)


]