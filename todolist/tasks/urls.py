from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('task list', views.task_lists, name='task_list'),
    path('create task', views.create_new, name='create_task'),
    path('update task/<int:task_id>', views.update_task, name='Update_task'),
    path('delete task/<int:task_pk>',views.delete_task, name = 'Delete_task'),
    path('login task',views.login_task, name = 'Login_task'),
    path('signup task',views.signup_task, name ='Signup_task'),
    path('logout task',views.logout_task, name ='Logout_task'),

]