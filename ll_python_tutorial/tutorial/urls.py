from django.urls import path

from . import views

urlpatterns = [
    path('read_chapters/<str:chapter_name>', views.read_chapters),
    path('read_chapters/', views.read_chapters),
    path('edit_chapters/<str:chapter_name>', views.new_chapter),
    path('edit_chapters/', views.new_chapter)
]