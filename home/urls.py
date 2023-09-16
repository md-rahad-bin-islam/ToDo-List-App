from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("create", views.create_item, name='create_item'),
    path("update/<int:id>", views.update_task, name='update'),
    path("destroy/<int:id>", views.destroy, name='destroy'),
    path("get-items/<int:id>", views.get_items, name='get-items'),

]
