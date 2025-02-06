from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = '/student'

class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = '/student'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_deleted.html'
    success_url = '/student'