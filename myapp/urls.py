from django.urls import path
from . import views
urlpatterns = [
    path ('signup/', views.signup, name='signup'),
    path ('', views.home, name='home'),
    path ('tasks/', views.tasks, name='tasks'),
    path ('logout/', views.signout, name='logout'),
    path ('signin/', views.signin, name='signin'),
    path ('create/task/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_details, name='task_details'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path ('tasks_completed', views.tasks_completed, name='tasks_completed'),


]