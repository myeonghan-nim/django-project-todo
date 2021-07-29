from django.urls import path

from . import views

urlpatterns = [
    # CREATE
    path('new/', views.new),
    path('create/', views.create),
    # READ
    path('', views.index),
    path('<int:todo_id>/detail', views.detail),
    # DELETE
    path('<int:todo_id>/delete/', views.delete),
    # UPDATE
    path('<int:todo_id>/edit/', views.edit),
    path('<int:todo_id>/update/', views.update),
]
