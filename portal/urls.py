from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('resources/', views.resources, name='resources'),
    path('courses/', views.courses, name='courses'),
    path('library/', views.library, name='library'),
    path('faq/', views.faq, name='faq'),
    path('api/update-activity/', views.update_user_activity, name='update_activity'),
    path('api/active-users/', views.get_active_users_count, name='active_users'),
]

