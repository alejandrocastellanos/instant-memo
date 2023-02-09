from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_notes, name="index"),
    path("<int:id>/edit/", views.edit_note, name="edit"),
    path("<int:id>/delete/", views.delete_note, name="delete"),
]
