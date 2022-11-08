from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("createpage", views.createPage, name="createpage"),
    path("create", views.create, name="create"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("update/<int:id>", views.update, name="update"),
    path("complete/<int:id>", views.complete, name="complete"),
    path("notcomplete/<int:id>", views.notComplete, name="notcomplete"),
]