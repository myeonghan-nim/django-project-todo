from django.urls import path
from . import views

urlpatterns = [
    # CREATE logic
    path('new/', views.new),
    path('create/', views.create),

    # READ logic
    path('', views.index),
    path('<int:todo_id>/detail', views.detail),

    # DELETE logic
    path('<int:todo_id>/delete/', views.delete),

    # UPDATE logic
    path('<int:todo_id>/edit/', views.edit),
    path('<int:todo_id>/update/', views.update),
]