from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentListView.as_view()),
    path('student/create/', views.StudentCreateView.as_view()),
    path('student/<int:pk>/update/', views.StudentUpdateView.as_view()),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view()),
]
