from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.display_todos, name = 'display'),
    path('add/', views.add_task, name = 'add'),
    path('display/task/<int:id>/', views.display_task, name = 'task'),
    path('todo_done/<int:id>/', views.mark_as_complete, name = 'done'),
    path('todo/category/<int:id>', views.display_by_category, name = 'category')
]
