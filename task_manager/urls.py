"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from tasks.views import GenericTaskDeleteView, GenericTaskDetailView, GenericTaskUpdateView, GenericTaskView, HomeView,  GenericTaskCreateView
from django.contrib.auth.views import LogoutView

from user.views import UserCreateView, UserLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view()),
    # AUTH
    path('user/login', UserLoginView.as_view()),
    path('user/signup', UserCreateView.as_view()),
    path('user/logout', LogoutView.as_view()),

    # Task
    path('tasks', GenericTaskView.as_view()),
    path('create-task', GenericTaskCreateView.as_view()),
    path('update-task/<pk>', GenericTaskUpdateView.as_view()),
    path('detail-task/<pk>', GenericTaskDetailView.as_view()),
    path('delete-task/<pk>', GenericTaskDeleteView.as_view()),
    # Hot Reload
    path("__reload__/", include("django_browser_reload.urls")),
]
