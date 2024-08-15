
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('tasks_pending', views.tasks, name='tasks_pending'),
    path('tasks_completed', views.tasks_completed, name='tasks_completed'),
    path('create/task', views.create_task, name='create_task'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('logout', views.signout, name='logout'),
    path('signin', views.signin, name='signin'),
]