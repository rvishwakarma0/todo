from django.urls import path
from . import views
urlpatterns = [
    path('',views.tasks, name="tasks"),
    path('new_task/',views.newTask, name="new_task"),
    path('update_task/<int:pk>/',views.updateTask, name="update_task"),
    path('delete_task/<int:pk>/',views.deleteTask, name="delete_task"),
    path('user_logout/',views.userLogout, name = "user_logout"),
    path('login_register/', views.loginOrRegister,name="login_register")
]