from django.urls import path

from todo import views

urlpatterns = [

    path('', views.TodoListView.as_view(), name='index'),
    path('add/', views.TodoCreateView.as_view(), name='todoAdd'),

    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', views.TodoUpdateView.as_view(), name='todo-edit'),

    path('completed/<todo_id>', views.todo_complete, name='complete'),
    path('delComplete/', views.delete_completed, name='completed-delete'),

    path('accounts/register/', views.register_page, name="register"),
    path('accounts/login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),

]
