"""ToDo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main, name ='main'),
    path('main/<int:list_id>/', views.singleList_view, name = 'single-list'), 
    path('<int:list_id>/', views.singleList_view), 
    path('', views.main),
    path('delete/<int:list_id>/', views.deleteList_view),
    path('main/delete/<int:list_id>/', views.deleteList_view),
    path('<int:list_id>/delete/<int:task_id>/', views.deleteTask_view),
    path('main/<int:list_id>/delete/<int:task_id>/', views.deleteTask_view),
    path('edit/<int:list_id>/', views.editList_view, name = 'edit-list'),
    path('main/edit/<int:list_id>', views.editList_view, name = 'edit-list'),
    path('<int:list_id>/edit/<int:task_id>/', views.editTask_view, name = 'edit-task'),
    path('main/<int:list_id>/edit/<int:task_id>/', views.editTask_view, name = 'edit-task'),
    path('<int:list_id>/<int:task_id>/move_to/<int:destinationList_id>/', views.moveTask_view, name = 'move-task'),
    path('main/<int:list_id>/<int:task_id>/move_to/<int:destinationList_id>/', views.moveTask_view, name = 'move-task')
]
